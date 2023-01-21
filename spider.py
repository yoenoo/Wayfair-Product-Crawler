import pandas as pd
from requests import Session

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int, required=True)
FLAGS,_ = parser.parse_known_args()


class WayfairProductCrawler:
	def __init__(self):
		self.base_url = "https://www.wayfair.com/graphql"

		headers = {
			"use-web-hash": "true",
			"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
		}	

		self.sess = Session()
		self.sess.headers.update(headers)

	def _get_products_by_category(self, category_id: int, page: int):
		hash = "22125c9a747b989fb251b014c2628213%23adda13419b757ac36f2b6c49a3bcd81c%23d0e1538c8199ca3253f0ba6c6f96b840%23f905cea77203534e928de4366ee3779d%2356bc66914e917daca7b7b6fbf0a6bcbb%2385a60692d411b1b94fcaf7e769b299f7%23937b5986d523ec2cd8ea2e68291b69e4%23226dd1f891ead00134d0c77687add073%23a928085179b4996abef8b881fc7887aa%23d878a5fca245086d6cd18dec8a364f30%2383d1f1132338d12cf533926fa527c5a7%233d54fb8f7ef35c34629aa853236e0fb2%23201c0252e9b59dc9bb102e35e1c303fe%2382032c3ee9d609c60f37d9172e2dfebe%2370ac03a548872795355b4b2d9ee86698%23c5a76122f3b3d9dddfaccf682f3c5e19%23adc79abec9f62457c811fbde536bcc59%23e5ba723f1dbb69724c115115fd923a47%23787e38482534a0d1832e19a21a36700e%239c61a681637cd2ae4bc71227fe3cf711%2348c76b09e216b294dd5eaba432f05598%23ddeed8a890c5e7e562f69812d05c1cc7"
		url = self.base_url + f"?hash={hash}"

		data = {
			"variables": {
				"categoryId": category_id,
				"usePricingField": "true",
				"browseInput": {
					"sortId": 7, # by customer rating
					"filters": [],
					"boostedSkus": [],
					"isAjax": "true",
					"skipLoadPricingModel": "false",
					"pagination": {"page": page, "itemsPerPage": 96},
				},
			}
		}

		resp = self.sess.post(url, json=data)
		resp.raise_for_status()
		return resp.json()

	def get_products_by_category(self, category_id: int): 
		page = 1
		out = []
		while page <= FLAGS.limit:
			results = self._get_products_by_category(category_id, page)
			category_hierarchy = [x["text"] for x in results["data"]["category"]["breadcrumbTrail"]]
			category_hierarchy_str = " > ".join(category_hierarchy)
			print(category_hierarchy_str)

			body = results["data"]["category"]["browse"]
			total_number_of_pages = body["pagination"]["total_number_of_pages"]
			current_page = body["pagination"]["current_page"]
			print(f"Total pages: {total_number_of_pages}")
			print(f"Current page: {current_page}")

			items = body.get("browse_grid_objects", [])
			for item in items:
				if item.get("__typename") == "Product":
					name = item.get("product_name")
					in_stock = item.get("inventory").get("stockStatus")
					avg_rating = item.get("customer_reviews").get("average_overall_rating")
					review_count = item.get("customer_reviews").get("review_count")
					manufacturer = item.get("manufacturer").get("name")
					sku = item.get("sku")
					price_block_elements = item.get("pricing").get("priceBlockElements")
					# TODO: needs to be improved... ranges, min, etc. 
					prices = {x.get("__typename"): x.get("display").get("value") for x in price_block_elements} 
					out.append([name, in_stock, avg_rating, review_count, manufacturer, sku, prices])

			# increment page 
			page += 1

		out = pd.DataFrame(out, columns=["name", "inStock", "avgReview", "reviewCount", "manufacturer", "sku", "prices"])
		out = pd.concat([
			out.drop("prices", axis=1),
			out["prices"].apply(pd.Series),
		], axis=1)
		return out

	def get_product_info(self, skus: list):
		hash = "e67bfa2d6bd7bcf6d8c351a68c4e18aa%2377c656652c1c4814baceb2546e8c8ff9%23cb05724590826da5c40607d51d79e079%2328c908fd3aa88467ecab787c0251bde9"
		url = self.base_url + f"?hash={hash}"

		data = {
			"variables": {
				"sku": skus[0],
				"additionalSkus": skus,
				"fullyConfigureOptions": "false",
			}
		}

		resp = self.sess.post(url, json=data)
		resp.raise_for_status()
		
		product_infos = resp.json().get("data", []).get("product", []).get("optionMatchedProducts", [])
		return product_infos



if __name__ == "__main__":
	crawler = WayfairProductCrawler()

	category_id = 414602
	products = crawler.get_products_by_category(category_id)
	print(products)

	product_infos = crawler.get_product_info(products["sku"].tolist())
	for i, product_info in enumerate(product_infos):
		sku = product_info["sku"]
		inventory = product_info["inventory"]["availableQuantity"]
		print(f"[{i}]", sku, inventory)
