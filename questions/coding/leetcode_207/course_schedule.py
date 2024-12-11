from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, num_courses: int, prereqs: List[List[int]]) -> bool:
        UNVISITED = 0 # No idea, I need to look into this.
        VISITING = 1 # Currently looking into this.
        VISITED = 2 # All good!
        states = [UNVISITED] * num_courses
        
        # building hash map
        hm = defaultdict(list)
        for course, prereq in prereqs:
            hm[prereq].append(course)
        # dfs
        def cycle_detection(course):
            if states[course] == VISITED: return False
            elif states[course] == VISITING:
                # Cycle detected!
                return True
            
            states[course] = VISITING

            for neighbor in hm[course]:
                if cycle_detection(neighbor):
                    return True
            
            states[course] = VISITED
            return False
        
        for course in range(num_courses):
            if cycle_detection(course): 
                return False
        
        return True
