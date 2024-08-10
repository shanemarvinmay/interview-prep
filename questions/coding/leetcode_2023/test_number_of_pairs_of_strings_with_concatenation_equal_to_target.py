from questions.coding.leetcode_2023.number_of_pairs_of_strings_with_concatenation_equal_to_target import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, target, expected', [
    (["777","7","77","77"], "7777", 4),
    (["123","4","12","34"], "1234", 2),
    (["1","1","1"], "11", 6),
])
def test_numOfPairs(nums, target, expected, sol):
    got = sol.numOfPairs(nums, target)

    assert got == expected

@pytest.mark.parametrize('num, target, expected', [
    ('34', '1234', '12'),
    ('12', '1234', '34'),
])
def test_get_sub_str(num, target, expected, sol):
    got = sol.get_sub_str(num, target)

    assert got == expected
