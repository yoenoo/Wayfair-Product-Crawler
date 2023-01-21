import json
import pandas as pd

with open("sample.json") as f:
	sample = json.load(f)

for item in sample["data"]["product"]["optionMatchedProducts"]:
	print(item["sku"])
	print(item["inventory"]["availableQuantity"])
	print(item["pricing"]["customerPrice"]["unitPrice"]["value"])
	print(item["pricing"]["listPrice"]["unitPrice"]["value"])

"""
with open("products.json") as f:
	products = json.load(f)

items = products["data"]["category"]["browse"]["browse_grid_objects"]
out = []
for item in items:
	if item.get("__typename") == "Product":
		name = item.get("product_name")
		in_stock = item.get("inventory").get("stockStatus")
		avg_rating = item.get("customer_reviews").get("average_overall_rating")
		review_count = item.get("customer_reviews").get("review_count")
		sku = item.get("sku")
		price_block_elements = item.get("pricing").get("priceBlockElements")
		prices = {x.get("__typename"): x.get("display").get("value") for x in price_block_elements}
		out.append([name, in_stock, avg_rating, review_count, sku, prices])

out = pd.DataFrame(out, columns=["name", "inStock", "avgReview", "reviewCount", "sku", "prices"])
out = pd.concat([
	out.drop("prices", axis=1),
	out["prices"].apply(pd.Series),
], axis=1)
print(out)
"""
