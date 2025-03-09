from questions.coding.leetcode_1718.construct_the_lexicographically_largest_valid_sequence import Solution

import pytest

@pytest.mark.parametrize('n, expected', [
    (1, [1]),
    (2, [2,1,2]),
    (3, [3,1,2,3,2]),
    (4, [4,2,3,2,4,3,1]),
    (5, [5,3,1,4,3,5,2,4,2]),
])
def test_constructDistancedSequence(n, expected):
    sol = Solution()

    got = sol.constructDistancedSequence(n)

    assert got == expected
