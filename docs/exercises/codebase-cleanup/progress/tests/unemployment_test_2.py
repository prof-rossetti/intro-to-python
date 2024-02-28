
# see also: https://github.com/prof-rossetti/codebase-cleanup-2021/pull/5/files

from app.unemployment import fetch_unemployment_data, ALPHAVANTAGE_API_KEY

import pytest
import requests_mock

#
# UNIT TESTS (using mock data to avoid a network request, can be run on CI)
#
# see: https://requests-mock.readthedocs.io/en/latest/pytest.html


mock_error_response = {
    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."
}

mock_rate_limit_response = {
    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."
}

mock_unemployment_response = {
    "name": "Unemployment Rate",
    "interval": "monthly",
    "unit": "percent",
    "data": [
        {
            "date": "2022-02-01",
            "value": "3.8"
        },
        {
            "date": "2022-01-01",
            "value": "4.0"
        },
        {
            "date": "2021-12-01",
            "value": "3.9"
        }
    ]
} # this is an abbreviated version of the real response


def test_fetch_data_using_mock_responses():

    # this is the real URL that gets requested
    request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"

    
    # TEST 1
    # the function should work as expected when the request is successful:
    with requests_mock.mock() as mocker:
        # shortcut to override the request and return some specified mock data
        mocker.get(request_url, json=mock_unemployment_response)

        # now we test the function in question
        data = fetch_unemployment_data()
        #breakpoint()

        assert isinstance(data, list)
        assert len(data) == 3

        latest_month = data[0]
        assert latest_month == {'date': '2022-02-01', 'value': '3.8'}

        
        
    # TEST 2
    # the function should fail gracefully when encountering a rate limit error:
    with requests_mock.mock() as mocker:
        # shortcut to override the request and return some specified mock data
        mocker.get(request_url, json=mock_rate_limit_response)

        # now we test the function in question
        data = fetch_unemployment_data()
        assert data == None
