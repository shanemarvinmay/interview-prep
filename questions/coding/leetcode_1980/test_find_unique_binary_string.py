from questions.coding.leetcode_1980.find_unique_binary_string import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    (["01","10"], '00'),
    (["00","01"], '10'),
    (["111","011","001"], '000')
])
def test_findDifferentBinaryString(nums, expected, sol):
    got = sol.findDifferentBinaryString(nums)

    assert got == expected
