import pytest

# import functions to be tested
from fuel import convert
from fuel import gauge

# Unit tests for convert function
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("70/100") == 70
    assert convert("1/3") == 33

def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("x/y")
    with pytest.raises(ValueError):
        convert("Test")
    with pytest.raises(ValueError):
        convert("x.y")

def test_convert_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

# Unit tests for guage function
def test_gauge_prec():
    assert gauge(50) == "50%"
    assert gauge(12) == "12%"

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
