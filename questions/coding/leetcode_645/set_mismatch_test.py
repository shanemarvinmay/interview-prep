from set_mismatch_solution import Solution

def test_find_set_mismatch():
    s = Solution()

    assert s.find_set_mismatch([2, 1, 4, 2]) == (2, 3)
