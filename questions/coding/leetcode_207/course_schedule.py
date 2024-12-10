from typing import List
from collections import deque
class Solution:
    def canFinish(self, num_courses: int, prereqs: List[List[int]]) -> bool:
        covered = set()
        hm = dict()

        # building hash map
        for i in range(num_courses):
            hm[i] = set()
            covered.add(i)
        for course, prereq in prereqs:
            if course in covered:
                covered.remove(course)
            hm[course].add(prereq)

        def bfs(course, seen=None):
            if seen is None:
                seen = set()
            q = deque([course])
            while q:
                v = q.popleft()
                if v in covered: continue
                covered.add(v)
                if v in seen: return True
                seen.add(v)
                for prereq in hm[v]:
                    q.append(prereq)
            return False
        
        for course in hm:
            if course in covered: continue
            cycle_detected = bfs(course)
            if cycle_detected: return False
        
        return len(covered) == num_courses
