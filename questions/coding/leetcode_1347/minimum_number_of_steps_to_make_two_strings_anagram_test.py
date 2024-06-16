from minimum_number_of_steps_to_make_two_strings_anagram_solution import Solution

import pytest

@pytest.mark.parametrize('message, s, t, expected', [
	('Unique counts and letters in each string.', 'leetcode', 'practice', 5),
	('Strings are anagrams.', "anagram","mangaar", 0)
])
def test_min_steps(message, s, t, expected):
	solution = Solution()

	assert solution.minSteps(s, t) == expected, message
