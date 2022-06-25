import pytest


# @pytest.mark.number
def test_type():
    assert type(11 + 56) is int


# @pytest.mark.number
def test_add_int():
    assert 15 + 15 == 20


@pytest.mark.skip(reason="Temporarily Disabled in string")
def test_string():
    assert "u" not in "Sumanth"


# @pytest.mark.string
def test_add_string():
    assert ("Mon" + "Day") == "MonDay"
