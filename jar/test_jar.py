import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(20)
    assert jar.capacity == 20
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(12)
    assert jar.deposit(2) == 2
    with pytest.raises(ValueError):
        jar.deposit(20)
    jar = Jar(100)
    assert jar.deposit(88) == 88
    assert jar.deposit(12) == 100
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    assert jar.withdraw(2) == 10
    assert jar.withdraw(10) == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
