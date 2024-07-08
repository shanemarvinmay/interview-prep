class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [1] * n

        i = 0
        while friends.count(1) != 1:
            if friends.count(1) == 0:
                friends = [1] * n
            i = self.get_next_idx(friends, i, k-1)
            friends[i] = 0

        return friends.index(1) + 1
    def get_next_idx(self, friends, i, k):
        n = len(friends)
        while friends[i] == 0:
            i = i+1 if i+1 < n else 0
        while k:
            i = i+1 if i+1 < n else 0
            if friends[i] == 0:
                continue
            k -= 1
        return i
