from questions.coding.leetcode_1415.the_kth_lexicographical_string_of_all_happy_strings_of_length_n import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('n, k, expected', [
    # (1,3,'c'),
    # (1,4,''),
    (2, 4, 'bc'),
    # (3,9, 'cab'),
    # (4, 10, "babc"),
    # (10, 100, "abacbabacb"),
])
def test_getHappyString(n, k, expected, sol):
    got = sol.getHappyString(n, k)

    assert got == expected