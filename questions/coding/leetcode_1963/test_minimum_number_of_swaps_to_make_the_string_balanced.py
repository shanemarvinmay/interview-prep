from questions.coding.leetcode_1963.minimum_number_of_swaps_to_make_the_string_balanced import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("][][", 1),
    ("]]][[[", 2),
    ("[]", 0),
    ("][][][", 1),
])
def test_minSwaps(s, expected):
    sol = Solution()

    got = sol.minSwaps(s)

    assert got == expected
