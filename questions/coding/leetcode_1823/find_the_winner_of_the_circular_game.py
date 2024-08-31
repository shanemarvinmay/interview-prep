class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winners = set()
        for i in range(1, n+1):
            winners.add(i)
        i = 1
        skips = k
        while len(winners) > 1:
            if i in winners:
                skips -= 1
            if skips == 0:
                winners.remove(i)
                skips = k
            i = 1 if i+1 > n else i+1

        return winners.pop()
