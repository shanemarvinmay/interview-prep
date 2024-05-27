from rearrange_array_elements_by_sign_solution import Solution


def test_rearrange_array():
	solution = Solution()
	nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
	expected = [28,-41,22,-8,46,-37,35,-9,18,-6,19,-26,15,-37,14,-10,31,-9]

	got = solution.rearrangeArray(nums)

	assert got == expected
