```
def allPathsSourceTarget(graph):
        
        #edges cases:
        if not graph:
            return []
        
        # build di-graph
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i] # one-way link
        
        # apply DFS on DAG
        n = len(graph)
        stack = [(0, [0])] # - store noth the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == n - 1:
                res.append(path)
            # traverse rest
            for nei in d[node]:
                stack.append((nei, path+[nei]))
        return res
    
```

[Link to solution.](https://leetcode.com/problems/all-paths-from-source-to-target/solutions/986429/python-iterative-dfs-with-detailed-time-complexity-visuals/)