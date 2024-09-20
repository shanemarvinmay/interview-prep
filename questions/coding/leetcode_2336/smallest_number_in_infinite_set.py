import heapq
class SmallestInfiniteSet:
    def __init__(self):
        self.next_inf = 1
        self.heap = []
    def popSmallest(self) -> int:
        # Return smallest from heap, if heap isn't empty and has the smallest num.
        if len(self.heap) and heapq.nsmallest(1, self.heap)[0] < self.next_inf:
            return heapq.heappop(self.heap)
        self.next_inf += 1
        return self.next_inf - 1
    def addBack(self, num: int) -> None:
        if num < self.next_inf and num not in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

'''
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[],                     [2],        [],            [],              [],          [1],       [],             [],            []]
[null,                  null,        1,            2,                3,           null,      1,               4,             5]
'''

if __name__ == '__main__': 
    li = [5, 7, 9, 1, 3]

    heapq.heapify(li)
    print(f"head init:{li}")

    heapq.heappush(li, 4)
    print(f"heap after pushing 4:{li}")

    sm = heapq.heappop(li)
    print(f"heap after popping smallest ({sm}):{li}")

    nsm = heapq.nsmallest(1, li)
    print(f"heap after looking nsmallest ({nsm}):{li}")

