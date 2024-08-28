from questions.coding.leetcode_1310.xor_queries_of_a_subarray import Solution

import pytest

@pytest.mark.parametrize('ar, queries, expected', [
    ([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]], [2,7,14,8]),
    ([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]], [8,0,4,4]),
])
def test_xorQueries(ar, queries, expected):
    sol = Solution()

    got = sol.xorQueries(ar, queries)

    assert got == expected
