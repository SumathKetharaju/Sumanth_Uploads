import math_func


def test_add_int():
    result = math_func.add(5, 2)
    assert result == 7


def test_add_float():
    result = math_func.add(3.2, 2.4)
    assert result == 5.6


def test_add_string():
    result = math_func.add("winter ", "season")
    assert result == "winter season"
