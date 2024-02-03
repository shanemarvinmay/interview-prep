'''Fenwick (BIT: Binary Index Tree)
example problems:
- https://www.geeksforgeeks.org/inversion-count-in-array-using-bit/
- https://www.geeksforgeeks.org/two-dimensional-binary-indexed-tree-or-fenwick-tree/
- https://www.geeksforgeeks.org/counting-triangles-in-a-rectangular-space-using-2d-bit/

Further info: 
- https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees
- google "python implement fenwick tree"
'''

class Fenwick_Tree:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(self.nums) + 1
        self.tree = [0] * self.size
        
        for i in range(len(self.nums)):
            self.update(i, self.nums[i])
    
    def update(self, idx, value):
        # Adjusting index since fenwick trees realy start at index 1.
        idx += 1

        while idx < self.size:
            self.tree[idx] += value
            # ? Update date idx from child to parent ?
            idx = idx + (idx & -idx)
    
    # TODO: get this to take in a start and ending idx to get the sum of.
    def get_sum(self, idx):
        total = 0
        # update idx since fenwick trees start at index 1
        idx += 1
        while idx > 0:
            total += self.tree[idx]
            idx = idx - (idx & -idx)
        
        return total

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    tree = Fenwick_Tree(nums)
    print(nums)
    print(tree.tree[1:])    
    for i in range(len(nums)):
        print(f'Sum from idx 0 to {i}:{tree.get_sum(i)}')
    print('Updating all nums so they go from 1 to 10')
    for i in range(len(nums)):
        diff = i + 1 - nums[i]
        nums[i] = i + 1
        tree.update(i, diff)
    print(nums)
    print(tree.tree[1:]) 
    for i in range(len(nums)):
        print(f'Sum from idx 0 to {i}:{tree.get_sum(i)}')