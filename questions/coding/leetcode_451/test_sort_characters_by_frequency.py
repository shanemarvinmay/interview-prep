from questions.coding.leetcode_451.sort_characters_by_frequency import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("tree", ["eert", "eetr"]),
    ("cccaaa",  ["aaaccc", "cccaaa"]),
    ("Aabb", ["bbAa", "bbaA"]),
])
def test_frequencySort(s, expected):
    sol = Solution()

    got = sol.frequencySort(s)

    assert got in expected
