from solution import Solution


def test_sol():
	solution = Solution()

	assert solution.maximumXOR([3,2,4,6]) == 7
	assert solution.maximumXOR([1,2,3,9,2]) == 11
	assert solution.maximumXOR([772,45,1,297,549,549,301,805,297,261,36,772,37,548,300,545,773,549,268,32,41,521,44,516,256,45,549]) == 813