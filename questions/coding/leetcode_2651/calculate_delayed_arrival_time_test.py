from calculate_delayed_arrival_time_solution import Solution

import pytest

@pytest.mark.parametrize('arrival_time, delay, expected', [(15, 5, 20), (15, 14, 5)])
def test_find_delayed_arrival_time(arrival_time, delay, expected):
    solution = Solution()

    assert solution.findDelayedArrivalTime(arrival_time, delay) == expected