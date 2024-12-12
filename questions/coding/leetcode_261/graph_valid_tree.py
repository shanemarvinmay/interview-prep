from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hm = dict()
        for v in range(n):
            hm[v] = set()
        for a, b in edges:
            hm[a].add(b)
            hm[b].add(a)
        
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * n

        def cycle_detected(v, prev=-1):
            if states[v] == VISITED:
                return False
            elif states[v] == VISITING:
                return True
            
            states[v] = VISITING

            for neighbor in hm[v]:
                # Make sure we don't go back and forth
                # on the same edge.
                if neighbor == prev: continue
                if cycle_detected(neighbor, prev=v): return True
            
            states[v] = VISITED
            return False
        
        if cycle_detected(0):
            return False
        
        return 0 not in states
