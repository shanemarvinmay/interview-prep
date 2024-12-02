from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_list = dict()
        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for s, e in pairs:
            if s not in adj_list:
                adj_list[s] = []
            adj_list[s].append(e)
            indegree[e] += 1
            outdegree[s] += 1
        
        start = None
        for node in outdegree:
            if outdegree[node] - indegree.get(node, 0) == 1:
                start = node
                break
        start = pairs[0][0] if start is None else start
        euler_path = []
        def dfs(vertex):
            while outdegree[vertex]:
                outdegree[vertex] -= 1
                next_vertex = adj_list[vertex][outdegree[vertex]]
                dfs(next_vertex)
            euler_path.append(vertex)
        dfs(start)
        euler_path.reverse()
        output = []
        for i in range(1, len(euler_path)):
            output.append([euler_path[i-1], euler_path[i]])
        return output