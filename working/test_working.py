import pytest

# import function to be tested
from working import convert

# unit tests for the various inputs
def test_convert_hr():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("6 PM to 1 AM") == "18:00 to 01:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("13 PM to 18 PM")
    with pytest.raises(ValueError):
        convert("6 AM to 13 AM")

def test_convert_hr_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("6:23 PM to 1:40 AM") == "18:23 to 01:40"
    assert convert("11:11 AM to 11:59 PM") == "11:11 to 23:59"
    assert convert("12:59 PM to 12:01 AM") == "12:59 to 00:01"
    with pytest.raises(ValueError):
        convert("11:60 PM to 8 AM")
    with pytest.raises(ValueError):
        convert("6:07 AM to 11:99 AM")

def test_convert_format():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("6 PM to 1:40 AM") == "18:00 to 01:40"
    with pytest.raises(ValueError):
        convert("11:00 PM - 8 AM")
    with pytest.raises(ValueError):
        convert("6:07 AM - 11:59 AM")
    with pytest.raises(ValueError):
        convert("9:07AM to 5:00PM")
    with pytest.raises(ValueError):
        convert("9:07 AM 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 07 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:07 AM to 5.00 PM")

