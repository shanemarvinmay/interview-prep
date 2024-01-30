from find_first_palindromic_string_in_the_array_solution import Solution

import pytest
'''
edge cases
no palindrome
        word
["def","ghi"]
        l r
multiple palindromes
              word
["abc","car","ada","racecar","cool"]
               l
               r
'''
@pytest.mark.parametrize('words, expected, message', [
    (["abc","car","ada","racecar","cool"], 'ada', 'Multiple palindromes.'),
    (["def","ghi"], '', 'No palindromes.')
])
def test_first_palindrome(words, expected, message):
    solution = Solution()

    assert solution.firstPalindrome(words) == expected, message