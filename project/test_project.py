import pytest
import cowsay

from project import valid_email, valid_pw, valid_login


# Unit tests for valid_email function
def test_valid_email():
    assert valid_email("david@harvard.edu") == "david@harvard.edu"
    assert valid_email("MALAN@harvard.edu") == "malan@harvard.edu"
    with pytest.raises(ValueError):
        valid_email("test@gmail.com")
    with pytest.raises(ValueError):
        valid_email("david.harvard.edu")
    with pytest.raises(ValueError):
        valid_email("David_Malan")

# Unit tests for valid_pw function
def test_valid_pw_valid():
    assert valid_pw("Test@12345678") == "Test@12345678"
    assert valid_pw("Tes@@1234567@") == "Tes@@1234567@"
    assert valid_pw("888888##Test") == "888888##Test"
    assert valid_pw("12#Test345678") == "12#Test345678"

def test_valid_pw_invalid():
    with pytest.raises(ValueError):
        valid_pw("Test1234567890")
    with pytest.raises(ValueError):
        valid_pw("Test@12345")
    with pytest.raises(ValueError):
        valid_pw("test@1234567890")
    with pytest.raises(ValueError):
        valid_pw("Test@ABCcefgh")
    with pytest.raises(ValueError):
        valid_pw("8822334455667700")
    with pytest.raises(ValueError):
        valid_pw("AbCdEfGhIjKl")

# Unit tests for valid_login function
def test_valid_login():
    assert valid_login("test@gmail.com", "Test@12345678") == f"{cowsay.get_output_string("cow", "Welcome to CS50!")}"
    assert valid_login("TEST@gmail.com", "Test@12345678") == f"{cowsay.get_output_string("cow", "Welcome to CS50!")}"
    with pytest.raises(ValueError):
        valid_login("test@gmail.com", "test@12345678")
    with pytest.raises(ValueError):
        valid_login("test@gmail.com", "12test@123456")
    with pytest.raises(ValueError):
        valid_login("test@harvard.edu", "Test@12345678")
