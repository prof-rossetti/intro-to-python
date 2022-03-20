




mock_error_response = {
    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."
}

mock_rate_limit_response = {
    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."
}

mock_msft_response = {
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "MSFT",
        "3. Last Refreshed": "2030-03-16",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2030-03-16": {
            "1. open": "236.2800",
            "2. high": "240.0550",
            "3. low": "235.9400",
            "4. close": "237.7100",
            "5. volume": "28092196"
        },
        "2030-03-15": {
            "1. open": "234.9600",
            "2. high": "235.1850",
            "3. low": "231.8100",
            "4. close": "234.8100",
            "5. volume": "26042669"
        },
        "2030-03-12": {
            "1. open": "234.0100",
            "2. high": "235.8200",
            "3. low": "233.2300",
            "4. close": "235.7500",
            "5. volume": "22653662"
        },
        "2030-03-11": {
            "1. open": "234.9600",
            "2. high": "239.1700",
            "3. low": "234.3100",
            "4. close": "237.1300",
            "5. volume": "29907586"
        },
        "2030-03-10": {
            "1. open": "237.0000",
            "2. high": "237.0000",
            "3. low": "232.0400",
            "4. close": "232.4200",
            "5. volume": "29746812"
        }
    }
}

mock_amzn_response = {
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "AMZN",
        "3. Last Refreshed": "2030-03-16",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2030-03-16": {
            "1. open": "3104.9700",
            "2. high": "3128.9100",
            "3. low": "3075.8601",
            "4. close": "3091.8600",
            "5. volume": "2538764"
        },
        "2030-03-15": {
            "1. open": "3074.5700",
            "2. high": "3082.2400",
            "3. low": "3032.0900",
            "4. close": "3081.6800",
            "5. volume": "2918592"
        },
        "2030-03-12": {
            "1. open": "3075.0000",
            "2. high": "3098.9800",
            "3. low": "3045.5000",
            "4. close": "3089.4900",
            "5. volume": "2421888"
        },
        "2030-03-11": {
            "1. open": "3104.0100",
            "2. high": "3131.7843",
            "3. low": "3082.9300",
            "4. close": "3113.5900",
            "5. volume": "2776391"
        },
        "2030-03-10": {
            "1. open": "3098.4500",
            "2. high": "3116.4600",
            "3. low": "3030.0500",
            "4. close": "3057.6400",
            "5. volume": "3012489"
        }
    }
}
