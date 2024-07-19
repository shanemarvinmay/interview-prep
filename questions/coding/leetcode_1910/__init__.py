from questions.coding.leetcode_1910.remove_all_occurrences_of_a_substring import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

'''
Example 2:
Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
Constraints:
1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.
'''
@pytest.mark.parametrize('s, p, expected', [
    ("daabcbaabcbc", "abc", "dab")
])
def test_removeOccurrences(s, p, expected, sol):
    got = sol.test_removeOccurrences(s, p)

    assert got == expected
