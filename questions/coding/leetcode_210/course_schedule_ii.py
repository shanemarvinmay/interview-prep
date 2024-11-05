from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Creating the maps.
        course_prereqs = dict()
        for i in range(numCourses):
            course_prereqs[i] = set()
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            course_prereqs[course].add(prereq)
        # Getting course order
        courses_seen = set()
        course_order = []
        old_len = 1
        while len(course_order) not in [old_len, numCourses]:
            old_len = len(course_order)
            for course, prereqs in course_prereqs.items():
                if course in courses_seen: continue
                if prereqs.issubset(courses_seen):
                    courses_seen.add(course)
                    course_order.append(course)
        if len(course_order) != numCourses:
            return []
        return course_order