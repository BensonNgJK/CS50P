import requests
import json
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(json.dumps(response.json(), indent=2))
