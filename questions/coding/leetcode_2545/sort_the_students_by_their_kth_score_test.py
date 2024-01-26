from sort_the_students_by_their_kth_score_solution import Solution

def test_sort_the_students():
    expected = [
        [7,5,11,2],
        [10,6,9,1],
        [4,8,3,15]
        ]
    scores = [
        [10,6,9,1],
        [7,5,11,2],
        [4,8,3,15]
        ]
    solution = Solution()

    assert solution.sortTheStudents(scores, 2) == expected
