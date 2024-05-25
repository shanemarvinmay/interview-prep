from collections import namedtuple
from number_of_students_unable_to_eat_lunch_solution import Solution

import pytest

EdgeCase = namedtuple('EdgeCase', 'students, sandwiches, expected, message')

@pytest.mark.parametrize('students, sandwiches, expected, message', [
    EdgeCase(students=[1,1,0,0], sandwiches=[0,1,0,1], expected=0, message='Every student eats.'),
    EdgeCase(students=[1,1,1,0,0,1], sandwiches=[1,0,0,0,1,1], expected=3, message='Some students don\'t eat')
])
def test_count_students(students, sandwiches, expected, message):
    solution = Solution()

    got = solution.countStudents(students, sandwiches)

    assert got == expected, message