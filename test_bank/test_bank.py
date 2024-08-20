import pytest

# Import function to be tested
from bank import value

# Unit Tests for various inputs
def test_value_hello():
    assert value("hello, there!") == 0
    assert value("HELLo") == 0
    assert value("HeLlO, :)") == 0

def test_value_with_h():
    assert value("hi, there!") == 20
    assert value("Hey!") == 20
    assert value("h3ll0, w0r1d!") == 20

def test_value_no_greeting():
    assert value("bye!") == 100
    assert value("= X") == 100
    assert value("Bonjour!~") == 100
    assert value("") == 100
