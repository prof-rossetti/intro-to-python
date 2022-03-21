


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"
url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(url)
parsed_response = json.loads(response.text)
#print(parsed_response)
#breakpoint()

tsd = parsed_response["Time Series (Digital Currency Daily)"]

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]
#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print('${:,.2f}'.format(float(latest['4a. close (USD)'])))
