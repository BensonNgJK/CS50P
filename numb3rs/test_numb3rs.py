import pytest

# import the function to be tested
from numb3rs import validate

# unit tests for valid number (0-255)
def test_validate_num():
    assert validate("275.1.100.222") == False
    assert validate("255.200.1.22") == True
    assert validate("0.1.200.0") == True
    assert validate("10.1000.10.255") == False
    assert validate("abc.250.222.21") == False
    assert validate("999.250.222.21") == False
    assert validate("200.275.275.275") == False


# unit tests for valid format
def test_validate_format():
    assert validate("0.0.0.0") == True
    assert validate("200.200.200") == False
    assert validate("2002550250") == False
    assert validate("250,200.1.22") == False
    assert validate("250.21.1.100.33") == False

