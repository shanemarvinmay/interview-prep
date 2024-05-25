from permutation_difference_between_two_strings_solution import Solution

def test_find_permutation_difference():
    solution = Solution()

    assert solution.findPermutationDifference('abc', 'bac') == 2
