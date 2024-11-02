from algorithms_data_structures.fibonacci.fibonacci import fibonacci

import pytest

@pytest.mark.parametrize('n, expected', [
    (5, 3), (-2, -1)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
