from generate_a_string_with_characters_that_have_odd_counts_solution import Solution

import pytest

@pytest.mark.parametrize('n, expected', [(3, 'aaa'), (2, 'ab')])
def test_generate_the_string(n, expected):
    solution = Solution()

    assert solution.generateTheString(n) == expected
