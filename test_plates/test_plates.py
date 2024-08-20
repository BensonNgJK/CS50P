import pytest

# import function to be tested
from plates import is_valid

# Unit Tests for the function
def test_is_valid_len():
    assert is_valid("CS50") == True
    assert is_valid("BA") == True
    assert is_valid("BA888877") == False
    assert is_valid("B") == False
    assert is_valid("") == False

def test_is_valid_letter():
    assert is_valid("B100") == False
    assert is_valid("BA9999") == True
    assert is_valid("WORLD") == True
    assert is_valid("9999BA") == False

def test_is_valid_num():
    assert is_valid("883366") == False
    assert is_valid("ABC888") == True
    assert is_valid("AB888C") == False
    assert is_valid("A8B8C7") == False
    assert is_valid("ABC088") == False
    assert is_valid("ABC808") == True

def test_is_valid_punc():
    assert is_valid("CS 50") == False
    assert is_valid("CS,50") == False
    assert is_valid("ABC50.") == False
