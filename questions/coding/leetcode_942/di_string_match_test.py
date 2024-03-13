from di_string_match_solution import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("IDID", [0,4,1,3,2]),
    ("III", [0,1,2,3]),
    ("DDI", [3,2,0,1])
])
def test_di_string_match(s, expected):
    solution = Solution()

    assert solution.diStringMatch(s) == expected