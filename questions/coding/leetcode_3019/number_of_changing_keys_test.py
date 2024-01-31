from number_of_changing_keys_solution import Solution

import pytest

@pytest.mark.parametrize('string, expected, message', [
    ('aAaAA', 0, 'No change.'),
    ('AaAbBb', 1, 'One change.'),
    ('abcb', 3, 'Multiple chages.')
])
def test_count_key_change(string, expected, message):
    solution = Solution()

    assert solution.countKeyChanges(string) == expected, message
