import pytest

from seasons import convert

# define unit tests for the function
def test_convert_valid():
    assert convert("2024-08-11") == 1440
    assert convert("2023-08-13") == 525600

def test_convert_invalid():
    with pytest.raises(SystemExit):
        convert("5 July 2024")
    with pytest.raises(SystemExit):
        convert("12-08-2023")
    with pytest.raises(SystemExit):
        convert("2023/08/12")
    with pytest.raises(SystemExit):
        convert("test")
