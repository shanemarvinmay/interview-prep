from rev_pos_int_solution import rev_pos_int

import pytest


@pytest.mark.parametrize('num, expected, message', [
    (123, 321, 'Int with no trailing zeros.'),
    (180, 81, 'Int with trailing zeros.'),
    (0, 0, 'Zero.')
])
def test_rev_pos_int(num, expected, message):
    assert rev_pos_int(num) == expected, message