from questions.coding.leetcode_406.queue_reconstruction_by_height import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('people, expected', [
    ([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]], [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]),
    ([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]], [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]),
    ([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]], [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]),
])
def test_reconstructQueue(people, expected, sol):
    got = sol.reconstructQueue(people)

    assert got == expected
