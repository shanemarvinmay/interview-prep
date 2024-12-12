from questions.coding.leetcode_261.graph_valid_tree import Solution

import pytest

@pytest.mark.parametrize('n, edges, expected, message', [
    (5, [[0,1],[0,2],[0,3],[1,4]], True, 'Valid tree.'),
    (5, [[0,1],[1,2],[2,3],[1,3],[1,4]], False, 'Cycle present.'),
    (1, [], True, 'Just the root.'),
    (3, [[0,1]], False, 'Disconnected graph.'),
    (4, [[0,1],[2,3]], False, 'Disconneted pairs.')
])
def test_validTree(n, edges, expected, message):
    sol = Solution()

    got = sol.validTree(n, edges)

    assert got == expected, message
