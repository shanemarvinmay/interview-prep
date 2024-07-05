from all_paths_from_source_to_target import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('graph, expected', [
   ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
   ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
])
def test_allPathsSourceTarget(graph, expected, sol):
    got = sol.allPathsSourceTarget(graph)
    if got != expected:
        for i in range(got):
            print(got[i])
            print(expected[i])
            print()
    assert got == expected