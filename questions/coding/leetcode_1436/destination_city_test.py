from destination_city_solution import Solution

import pytest


@pytest.mark.parametrize('paths, expected', [
    ([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]], "Sao Paulo"),
    ([["B","C"],["D","B"],["C","A"]], "A")
])
def test_dest_city(paths, expected):
    solution = Solution()
    assert solution.destCity(paths) == expected