

print("UNEMPLOYMENT REPORT...")


import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_unemployment_data():
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    #return parsed_response["data"]

    # handle rate limits where the expected structure is not there
    # can use try/except block, or conditional to check if "data" in list(parsed_response.keys())
    try:
        return parsed_response["data"]
    except:
        return None



if __name__ == "__main__":

    # ....
