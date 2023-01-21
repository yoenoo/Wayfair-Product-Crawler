curl 'https://www.wayfair.com/graphql?hash=22125c9a747b989fb251b014c2628213%23adda13419b757ac36f2b6c49a3bcd81c%23d0e1538c8199ca3253f0ba6c6f96b840%23f905cea77203534e928de4366ee3779d%2356bc66914e917daca7b7b6fbf0a6bcbb%2385a60692d411b1b94fcaf7e769b299f7%23937b5986d523ec2cd8ea2e68291b69e4%23226dd1f891ead00134d0c77687add073%23a928085179b4996abef8b881fc7887aa%23d878a5fca245086d6cd18dec8a364f30%2383d1f1132338d12cf533926fa527c5a7%233d54fb8f7ef35c34629aa853236e0fb2%23201c0252e9b59dc9bb102e35e1c303fe%2382032c3ee9d609c60f37d9172e2dfebe%2370ac03a548872795355b4b2d9ee86698%23c5a76122f3b3d9dddfaccf682f3c5e19%23adc79abec9f62457c811fbde536bcc59%23e5ba723f1dbb69724c115115fd923a47%23787e38482534a0d1832e19a21a36700e%239c61a681637cd2ae4bc71227fe3cf711%2348c76b09e216b294dd5eaba432f05598%23ddeed8a890c5e7e562f69812d05c1cc7' \
  -H 'use-web-hash: true' \
	-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
  --data-raw '{"variables":{"categoryId":414602,"browseInput":{"sortId":186,"filters":[{"filterStringUnencoded":"a75128~442165"},{"filterStringUnencoded":"a13098~5"},{"filterStringUnencoded":"a13098~4"}],"pagination":{"page":3,"itemsPerPage":48},"boostedSkus":[],"isAjax":true,"skipLoadPricingModel":false},"usePricingField":true},"_pageId":"SwH766+FNb5qOoBo9UrufQ==","_isPageRequest":true}'




#curl 'https://www.wayfair.com/graphql?hash=22125c9a747b989fb251b014c2628213%23adda13419b757ac36f2b6c49a3bcd81c%23d0e1538c8199ca3253f0ba6c6f96b840%23f905cea77203534e928de4366ee3779d%2356bc66914e917daca7b7b6fbf0a6bcbb%2385a60692d411b1b94fcaf7e769b299f7%23937b5986d523ec2cd8ea2e68291b69e4%23226dd1f891ead00134d0c77687add073%23a928085179b4996abef8b881fc7887aa%23d878a5fca245086d6cd18dec8a364f30%2383d1f1132338d12cf533926fa527c5a7%233d54fb8f7ef35c34629aa853236e0fb2%23201c0252e9b59dc9bb102e35e1c303fe%2382032c3ee9d609c60f37d9172e2dfebe%2370ac03a548872795355b4b2d9ee86698%23c5a76122f3b3d9dddfaccf682f3c5e19%23adc79abec9f62457c811fbde536bcc59%23e5ba723f1dbb69724c115115fd923a47%23787e38482534a0d1832e19a21a36700e%239c61a681637cd2ae4bc71227fe3cf711%2348c76b09e216b294dd5eaba432f05598%23ddeed8a890c5e7e562f69812d05c1cc7' \
#  -H 'authority: www.wayfair.com' \
#  -H 'accept: application/json' \
#  -H 'accept-language: ko-KR,ko;q=0.9' \
#  -H 'apollographql-client-name: @wayfair/sf-ui-browse' \
#  -H 'apollographql-client-version: eb710aaa423bbd41bdf30809e441a0fe11c464b5' \
#  -H 'cache-control: no-cache' \
#  -H 'content-type: application/json' \
#  -H 'origin: https://www.wayfair.com' \
#  -H 'pragma: no-cache' \
#  -H 'referer: https://www.wayfair.com/filters/furniture/sb3/coffee-tables-c414602-a13098~4-a13098~5-a75128~442165.html?curpage=2' \
#  -H 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
#  -H 'sec-ch-ua-mobile: ?0' \
#  -H 'sec-ch-ua-platform: "macOS"' \
#  -H 'sec-fetch-dest: empty' \
#  -H 'sec-fetch-mode: cors' \
#  -H 'sec-fetch-site: same-origin' \
#  -H 'use-web-hash: true' \
#  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' \
#  -H 'x-parent-txid: I/WEwmPLE8ylVqKV04F0Ag==' \
#  --data-raw '{"variables":{"categoryId":414602,"browseInput":{"sortId":186,"filters":[{"filterStringUnencoded":"a75128~442165"},{"filterStringUnencoded":"a13098~5"},{"filterStringUnencoded":"a13098~4"}],"pagination":{"page":3,"itemsPerPage":48},"boostedSkus":[],"isAjax":true,"skipLoadPricingModel":false},"usePricingField":true},"_pageId":"SwH766+FNb5qOoBo9UrufQ==","_isPageRequest":true}' \
#  --compressed > products.json
