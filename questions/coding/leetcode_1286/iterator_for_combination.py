from collections import deque

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.chars = ''.join(sorted(characters))
        self.length = combinationLength
        self.combos = deque()
        self.get_combos([], -1)
    def next(self) -> str:
        return self.combos.popleft()
    def hasNext(self) -> bool:
        return len(self.combos) > 0
    def get_combos(self, cur: list[str], idx: int):
        if len(cur) == self.length:
            self.combos.append(''.join(cur))
            return
        for i in range(idx + 1, len(self.chars)):
            cur.append(self.chars[i])
            self.get_combos(cur, i)
            cur.pop()
'''
1286. Iterator for Combination
https://leetcode.com/problems/iterator-for-combination/
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]
Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
'''
# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()