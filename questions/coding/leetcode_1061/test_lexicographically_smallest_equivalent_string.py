from questions.coding.leetcode_1061.lexicographically_smallest_equivalent_string import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('s1, s2, baseStr, expected', [
    ("parker",  "morris",  "parser","makkek"),
    ("hello", "world", "hold", "hdld"),
    ("leetcode", "programs", "sourcecode", "aauaaaaada"),
    ("cgokcgerolkgksgbhgmaaealacnsshofjinidiigbjerdnkolc", "rjjlkbmnprkslilqmbnlasardrossiogrcboomrbcmgmglsrsj", "bxbwjlbdazfejdsaacsjgrlxqhiddwaeguxhqoupicyzfeupcn", "axawaaaaazaaaaaaaaaaaaaxaaaaawaaauxaaauaaayzaauaaa"),
])
def test_smallestEquivalentString(s1, s2, baseStr, expected, sol):
    got = sol.smallestEquivalentString(s1, s2, baseStr)

    assert got == expected