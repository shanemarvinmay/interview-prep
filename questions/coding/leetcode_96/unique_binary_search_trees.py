class Solution:
    def __init__(self):
        self.nodes_to_sub_count = {0:1, 1:1, 2:2, 3:5}
    def numTrees(self, n: int, root=-1) -> int:
        if n in self.nodes_to_sub_count:
            return self.nodes_to_sub_count[n]
        if root != -1:
            if root in self.nodes_to_sub_count:
                return self.nodes_to_sub_count[root]
            else:
                n = root
        
        count = 0
        for i in range(1,n+1):
            count += self.numTrees(n,i-1) * self.numTrees(n,n-i)
        
        self.nodes_to_sub_count[n] = count
        return self.nodes_to_sub_count[n]