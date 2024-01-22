from minimum_number_of_operations_to_move_all_balls_to_each_box_solution import Solution


def test_min_operations():
    s = Solution()

    assert s.min_operations('001011') == [11, 8, 5, 4, 3, 4]