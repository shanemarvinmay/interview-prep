from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_preferences = [0, 0]
        for student in students:
            student_preferences[student] += 1
        
        for sandwich in sandwiches:
            if student_preferences[sandwich] == 0:
                return sum(student_preferences)
            student_preferences[sandwich] -= 1
        
        return 0
