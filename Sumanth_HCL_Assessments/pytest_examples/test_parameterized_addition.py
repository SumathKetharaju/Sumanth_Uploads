import pytest
import math_func


@pytest.mark.parametrize("input_1, input_2, result", [(20, 30, 50), (20.4, 30.6, 51), ("winter", " season", "winter season")])
def test_add(input_1, input_2, result):
    assert math_func.add(input_1, input_2) == result
