from questions.coding.leetcode_3243.shortest_distance_after_road_addition_queries_i import Solution

import pytest

@pytest.mark.parametrize('n, queries, expected', [
    (5, [[2,4],[0,2],[0,4]], [3,2,1]),
    (4, [[0,3],[0,2]], [1,1]),
    (6, [[0,2],[1,5]],[4,2])
])
def test_shortestDistanceAfterQueries(n, queries, expected):
    sol = Solution()

    got = sol.shortestDistanceAfterQueries(n, queries)

    assert got == expected