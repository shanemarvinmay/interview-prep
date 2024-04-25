from check_if_all_characters_have_equal_number_of_occurrences_solution import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ('abcabc', True),
('aabc', False)
])
def test_are_occurences_equal(s, expected):
    solution = Solution()

    assert solution.areOccurrencesEqual(s) == expected