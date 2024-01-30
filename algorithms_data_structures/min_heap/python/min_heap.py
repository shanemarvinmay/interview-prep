'''
cur node = ar[i]
parent node = ar[ (i - 1) / 2 ]
left child = ar[ 2*i + 1 ]
right child = ar[ 2*i + 2 ]

root = ar[0]
'''
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx - 1) // 2
    
    def left_child(self, idx):
        return 2 * idx + 1
    
    def right_child(self, idx):
        return 2 * idx + 2
    
    def get_min(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)

        cur = len(self.heap) - 1
        while cur > 0 and self.heap[self.parent(cur)] > self.heap[cur]:
            # Swap
            self.heap[cur], self.heap[self.parent(cur)] = self.heap[self.parent(cur)], self.heap[cur]
            cur = self.parent(cur)

    def pop_min(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return value

    def heapify(self, idx):
        left = self.left_child(idx)
        right = self.right_child(idx)
        smallest = idx

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.heapify(smallest)
