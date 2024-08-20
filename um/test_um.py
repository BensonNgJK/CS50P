import pytest

# import function to be tested
from um import count

# define unit tests for the function
def test_count_valid_um():
    assert count("um.. hello, UM") == 2
    assert count("Um.. Yummy!") == 1
    assert count("Umm Um.. Um, Okay!") == 2
    assert count("hello, um.. Can you help me?") == 1

def test_count_um_word():
    assert count("um... Yummy!") == 1
    assert count("Yum, Yum, Yum") == 0
    assert count("Um.. Rmb to bring an umbrella.") == 1
    assert count("um.. Um.. UM.. Yum, Yummy!") == 3

def test_count_no_um():
    assert count("") == 0
    assert count("Hello, there!") == 0
    assert count("... ... ...") == 0
    assert count("um123, 321um") == 0
