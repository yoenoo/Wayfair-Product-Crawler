import requests

# url = "https://www.wayfair.com/furniture/sb0/sectionals-c413893.html"
url = "https://www.wayfair.com/graphql?hash=127b34c1fce6c2f7197c166e7596cbae"

headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

data = {
	"variables": {
		"sku": "W005114537",
		"selectedOptionIds": ["0", "0"],
	}
}
import json
data = json.dumps(data)

resp = requests.post(url, headers=headers, data=data) 
resp.raise_for_status()
print(resp.text)
