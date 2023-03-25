import calculations
import pytest

# Parameterizing the test cases
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (-1, -2, -3),
        (-1, 0, -1),
        (-1, 1, 0),
        (1000, 1, 1000)
    ])
def test_add(num1, num2, expected):
    # assert 8==calculations.add(3,5)
    assert calculations.add(num1, num2)==expected






