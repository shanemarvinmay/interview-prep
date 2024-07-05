from typing import List

class Solution:
    def __init__(self):
        self.paths = []
        self.terminal_node = 0

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.paths = []
        self.terminal_node = len(graph) - 1
        self.fill_paths(graph)
        return self.paths
        
    def fill_paths(self, graph, cur_node=0, path=None):
        if path is None:
            path = []

        path.append(cur_node)

        if cur_node == self.terminal_node:
            self.paths.append(path)
            
        for node in graph[cur_node]:

            self.fill_paths(graph, node, path[:])