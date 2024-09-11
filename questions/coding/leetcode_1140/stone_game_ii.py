from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        greatest_alice, _ = self.help(piles)
        return greatest_alice
    def help(self, piles: List[int], idx=0, alice=0, bob=0, alices_turn=True):
        if idx >= len(piles):
            return alice, bob
        alice1 = alice2 = alice
        bob1 = bob2 = bob
        # Taking 2.
        if idx + 1 < len(piles):
            if alices_turn:
                new_alice = alice + piles[idx] + piles[idx+1]
                alice2, bob = self.help(piles, idx+2, new_alice, bob, not alices_turn)
            else:
                new_bob = bob + piles[idx] + piles[idx+1]
                alice, bob2  = self.help(piles, idx+2, alice, new_bob, not alices_turn)
        # Taking 1
        if alices_turn:
            new_alice = alice + piles[idx]
            alice1, bob = self.help(piles, idx+1, new_alice, bob, not alices_turn)
        else:
            new_bob = bob + piles[idx]
            alice, bob1  = self.help(piles, idx+1, alice, new_bob, not alices_turn)
        return max(alice1, alice2), max(bob1, bob2)

'''
1140. Stone Game II
https://leetcode.com/problems/stone-game-ii/
Input: piles = 
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
Example 2:
Input: piles = 
'''