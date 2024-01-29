from partition_array_according_to_given_pivot_solution import Solution

def test_pivot_array():
    nums = [9,12,5,10,14,3,10]
    pivot = 10
    expected = [9,5,3,10,10,12,14]
    solution = Solution()

    got = solution.pivotArray(nums, pivot)

    assert got == expected
