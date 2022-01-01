"""You’ve probably looked up conversion rates using your browser,
 but here’s how to automate the task of finding the current exchange rate between any two currencies."""

import json
import sys
import urllib.request

if len(sys.argv) != 3:
    print("Usage: ./currencyrates.py lookup_currency base_currency. Example: ./currencyrates.py cad usd")
    sys.exit()

currency = sys.argv[1]
base_currency = sys.argv[2]

currency_url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + base_currency + "&v=1&s=cbr"
f = urllib.request.urlopen(currency_url)
obj = json.loads(f.read())
result = "1 " + currency.upper() + " is "
result += "{:,.2f}".format(1/obj[currency.upper()]) + " " + base_currency.upper()

print(result)
