from sum_of_digits_in_base_k_solution import Solution

def test_sum_base():
    solution = Solution()

    # Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
    assert solution.sumBase(34, 6) == 9
