class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        components = 0
        # Building adj list
        adj = dict()
        for i in range(n):
            adj[i] = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(root, prev):
            nonlocal components
            if root is None: return 0
            total = values[root]
            for child in adj[root]:
                if child == prev: continue
                total += dfs(child, root)
            remainder = total % k
            if remainder == 0:
                components += 1
            return remainder
        
        dfs(root=0, prev=-1)

        return components
