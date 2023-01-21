import requests
import pandas as pd 
from pprint import pprint

sku = "W007425536"

base_url = "https://www.wayfair.com/graphql" 
hash = "e67bfa2d6bd7bcf6d8c351a68c4e18aa%2377c656652c1c4814baceb2546e8c8ff9%23cb05724590826da5c40607d51d79e079%2328c908fd3aa88467ecab787c0251bde9"
url = base_url + f"?hash={hash}"

headers = {
	"use-web-hash": "true",
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

data = {
	"variables": {
		"sku": sku,
		"additionalSkus": [sku],
		"fullyConfigureOptions": "false",
	}
}

resp = requests.post(url, headers=headers, json=data)
resp.raise_for_status()

products = resp.json()["data"]["product"]["optionMatchedProducts"]
for product in products:
	inventory = product["inventory"]["availableQuantity"]
	print(sku, inventory)
