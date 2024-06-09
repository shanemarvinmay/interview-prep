from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
		# Make a queue from containing the largest number.
        q = deque([deck.pop()])
        
		# Adding cards and reordering.
        while len(deck):
            # Moving last card to front of the queue.
            new_front = q.pop()
            q.appendleft(new_front)
            # Adding next biggest card from the deck to the front of the queue.
            q.appendleft(deck.pop())
    
        return list(q)