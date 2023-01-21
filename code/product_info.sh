curl 'https://www.wayfair.com/graphql?hash=e67bfa2d6bd7bcf6d8c351a68c4e18aa%2377c656652c1c4814baceb2546e8c8ff9%23cb05724590826da5c40607d51d79e079%2328c908fd3aa88467ecab787c0251bde9' \
  -H 'use-web-hash: true' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
  --data-raw '{"variables":{"sku":"W007425536","additionalSkus": ["W007425536"], "fullyConfigureOptions":false}}' 


#curl 'https://www.wayfair.com/graphql?hash=e67bfa2d6bd7bcf6d8c351a68c4e18aa%2377c656652c1c4814baceb2546e8c8ff9%23cb05724590826da5c40607d51d79e079%2328c908fd3aa88467ecab787c0251bde9' \
#  -H 'authority: www.wayfair.com' \
#  -H 'accept: application/json' \
#  -H 'accept-language: ko-KR,ko;q=0.9' \
#  -H 'apollographql-client-name: @wayfair/sf-ui-product-details' \
#  -H 'apollographql-client-version: 7128a20d2b845b47c2ed7374a9f401295a8b2fe0' \
#  -H 'cache-control: no-cache' \
#  -H 'content-type: application/json' \
#  -H 'origin: https://www.wayfair.com' \
#  -H 'pragma: no-cache' \
#  -H 'referer: https://www.wayfair.com/furniture/pdp/gracie-oaks-haneline-lift-top-4-legs-coffee-table-with-storage-w006110279.html?piid=1002536401' \
#  -H 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
#  -H 'sec-ch-ua-mobile: ?0' \
#  -H 'sec-ch-ua-platform: "macOS"' \
#  -H 'sec-fetch-dest: empty' \
#  -H 'sec-fetch-mode: cors' \
#  -H 'sec-fetch-site: same-origin' \
#  -H 'use-web-hash: true' \
#  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
#  -H 'x-parent-txid: I/WEwmPLFZ9lRrIcjo2JAg==' \
#  --data-raw '{"variables":{"sku":"W007425536","additionalSkus": ["W007425536"], "fullyConfigureOptions":false}}' \
#  --compressed > sample.json
