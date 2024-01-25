from decrypt_string_from_alphabet_to_integer_mapping_solution import Solution

import pytest

@pytest.mark.parametrize('input_string, expected', [('10#11#12', 'jkab'), ('1326#', 'acz')])
def test_freq_alphabets(input_string, expected):
    solution = Solution()

    assert solution.freqAlphabets(input_string) == expected