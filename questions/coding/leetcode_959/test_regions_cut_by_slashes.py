from questions.coding.leetcode_959.regions_cut_by_slashes import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([
        " /",
        "/ "
    ], 2),
    ([
        " /",
        "  "
    ], 1),
    ([
        "/\\",
        "\\/"
    ], 5),
    ([
        "\\/",
        "/\\"
    ], 4),
    ([' / \\ '], 3),
])
def test_regionsBySlashes(grid, expected):
    sol = Solution()

    got = sol.regionsBySlashes(grid)

    assert got == expected
