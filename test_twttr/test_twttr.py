import pytest

# import function to be tested
from twttr import shorten

# define functions for testing shorten

def test_vowels_lower():
    assert shorten("twitter.com") == "twttr.cm"
    assert shorten("just setting") == "jst sttng"

def test_vowels_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("JUST SETTING") == "JST STTNG"

def test_vowels_mix():
    assert shorten("TWItter") == "TWttr"
    assert shorten("JUST Setting") == "JST Sttng"

def test_no_vowels():
    assert shorten("cs.888") == "cs.888"
    assert shorten("CS50") == "CS50"
