
#
# function definition and usage in a script:
#

from datetime import datetime

def human_friendly(my_datetime):
    """
    Converts a date time object into a human-friendly string

    Param: my_datetime (datetime.datetime object)
    """
    formatted_datestring = my_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return f"Checkout at: {formatted_datestring}"

if __name__ == "__main__":
    print(human_friendly(datetime.now()))

#
# corresponding test:
#

from datetime import datetime

def test_human_friendly():
    mock_datetime = datetime(2020, 3, 27, 13, 47, 25) # assemble an example datetime object
    assert human_friendly(mock_datetime) == "Checkout at: 2020-03-27 13:47:25"
