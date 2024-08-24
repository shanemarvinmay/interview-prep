from questions.coding.leetcode_3159.find_occurrences_of_an_element_in_an_array import Solution

import pytest

@pytest.mark.parametrize('nums, queries, x, expected', [
    ([1,3,1,7], [1,3,2,4], 1, [0,-1,2,-1]),
    ([1,2,3], [10], 5, [-1]),
])
def test_occurrencesOfElement(nums, queries, x, expected):
    sol = Solution()

    got = sol.occurrencesOfElement(nums, queries, x)

    assert got == expected
