from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers, multi_losers = set(), set(), set()

        for match in matches:
            winner, loser = match
            winners.add(winner)
            if loser in losers:
                multi_losers.add(loser)
            losers.add(loser)
        
        winners = winners.difference(losers)
        single_losers = losers.difference(multi_losers)

        winners = sorted(list(winners))
        single_losers = sorted(list(single_losers))
        return [winners, single_losers]
