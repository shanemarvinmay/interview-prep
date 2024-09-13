from questions.coding.leetcode_893.groups_of_special_equivalent_strings import Solution

import pytest

@pytest.mark.parametrize('words, expected', [
    (["abcd","cdab","cbad","xyzz","zzxy","zzyx"], 3),
    (["abc","acb","bac","bca","cab","cba"], 3),
])
def test_numSpecialEquivGroups(words, expected):
    sol = Solution()

    got = sol.numSpecialEquivGroups(words)

    assert got == expected
