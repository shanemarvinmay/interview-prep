from selection_sort import Solution

def test_selection_sort():
	expected = [0,1,2]
	nums = [2,0,1]
	solution = Solution()

	assert solution.sortColors(nums) == expected