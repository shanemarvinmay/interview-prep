from score_a_string_solution import Solution

import pytest

@pytest.mark.parametrize('string, expected, message', [
    ('hello', 13, 'Normal string.'),
    ('a', 0, 'One or less characters.')
])
def test_score_of_string(string, expected, message):
    solution = Solution()

    got = solution.scoreOfString(string)

    assert got == expected, message