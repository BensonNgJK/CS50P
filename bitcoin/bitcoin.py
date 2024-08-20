# Import required libraries/functions
import requests
import sys
import json

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bpi = response.json()
    print(json.dumps(response.json(), indent=2))
    price_usd = bpi["bpi"]["USD"]["rate_float"]
    if len(sys.argv) == 2:
        print(f"${float(sys.argv[1])*price_usd:,.4f}")
    else:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("Request Error")
