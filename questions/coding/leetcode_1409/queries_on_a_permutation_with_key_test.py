from queries_on_a_permutation_with_key_solution import *

import pytest

@pytest.mark.parametrize('queries, m, expected', [
    ([3,1,2,1], 5, [2,1,2,1]),
    ([4,1,2,2], 4, [3,1,2,0]),
    ([7,5,5,8,3], 8, [6,5,0,7,5])
])
def test_process_queries(queries, m, expected):
    solution = Solution()

    got = solution.processQueries(queries, m)

    assert got == expected
