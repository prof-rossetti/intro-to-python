

from app.unemployment import fetch_unemployment_data


#
# INTEGRATION TESTS (END TO END, may need to be skipped on CI)
#

def test_fetch_data():

    data = fetch_unemployment_data()
    #breakpoint()

    # expecting the data to be a list of dictionaries
    assert isinstance(data, list)

    # expecting lots of months worth of data
    assert len(data) > 800

    # the latest month will change over time, so we maybe won't be able to test the exact values,
    # ... but we can test the structure (for example, the expected keys and their datatypes):

    latest_month = data[0] #> something like {'date': '2022-02-01', 'value': '3.8'}
    assert isinstance(latest_month, dict)
    assert sorted(list(latest_month.keys())) == ["date", "value"]

    assert isinstance(latest_month["date"], str)
    assert isinstance(latest_month["value"], str)

