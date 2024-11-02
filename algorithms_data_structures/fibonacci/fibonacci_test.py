from algorithms_data_structures.fibonacci.fibonacci import fibonacci, fibonacci_recursive

import pytest

@pytest.mark.parametrize('n, expected', [
    (6, 8), (-2, -1)
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected
    assert fibonacci_recursive(n) == expected
