from find_the_number_of_good_pairs_i_solution import Solution

def test_number_of_pairs():
	expected = 5
	solution = Solution()
	nums1 = [1,3,4]
	nums2 = [1,3,4]
	k = 1
	
	got = solution.numberOfPairs(nums1, nums2, k)

	assert got == expected
