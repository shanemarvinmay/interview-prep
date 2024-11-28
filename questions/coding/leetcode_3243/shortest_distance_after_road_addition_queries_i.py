from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        graph = dict()
        # Setting up graph
        for i in range(n):
            graph[i] = {'upstream': [], 'min_steps': n-i-1}
            if i:
                graph[i]['upstream'].append(i-1)

        def update_upstream(s, min_steps):
            for v in graph[s]['upstream']:
                if min_steps + 1 < graph[v]['min_steps']:
                    graph[v]['min_steps'] = min_steps + 1
                    update_upstream(v, min_steps+1)
        # Finding min distances after new roads are added.
        for s, e in queries:
            if graph[e]['min_steps'] + 1 < graph[s]['min_steps']:
                graph[s]['min_steps'] = graph[e]['min_steps'] + 1
                update_upstream(s, graph[s]['min_steps'])
            graph[e]['upstream'].append(s)
            ans.append(graph[0]['min_steps'])

        return ans
    