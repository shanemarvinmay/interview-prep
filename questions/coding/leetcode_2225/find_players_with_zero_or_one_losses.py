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

'''


Input: matches = 
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:
Input: matches = 
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
Constraints:
1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.
'''