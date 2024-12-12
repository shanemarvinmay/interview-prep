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

        def cycle_detected(v, history = None):
            if states[v] == VISITED:
                return False
            elif states[v] == VISITING:
                return True
            if history is None:
                history = []
            
            states[v] = VISITING
            history.append(v)


            for neighbor in hm[v]:
                # Make sure we don't go back and forth
                # on the same edge.
                if len(history) > 1 and neighbor == history[-2]: continue
                if cycle_detected(neighbor, history): return True
            
            states[v] = VISITED
            history.pop()
            return False
        
        if cycle_detected(0):
            return False
        
        return 0 not in states
