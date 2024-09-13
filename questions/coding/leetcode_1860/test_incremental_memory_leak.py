from questions.coding.leetcode_1860.incremental_memory_leak import Solution

import pytest

@pytest.mark.parametrize('m1, m2, expected', [
    (2, 2, [3,1,0]),
    (8, 11, [6,0,4]),
])
def test_memLeak(m1, m2, expected):
    sol = Solution()

    got = sol.memLeak(m1, m2)

    assert got == expected
'''

Input: memory1 = 2, memory2 = 2
Output: 
Explanation: The memory is allocated as follows:
- At the 1st second, 1 bit of memory is allocated to stick 1. The first stick now has 1 bit of available memory.
- At the 2nd second, 2 bits of memory are allocated to stick 2. The second stick now has 0 bits of available memory.
- At the 3rd second, the program crashes. The sticks have 1 and 0 bits available respectively.
Example 2:

Input: memory1 = 8, memory2 = 11
Output: '''