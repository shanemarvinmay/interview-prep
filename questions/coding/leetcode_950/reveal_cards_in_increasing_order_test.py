from reveal_cards_in_increasing_order_solution import Solution

import pytest

@pytest.mark.parametrize("deck, expected", [
	([1,2,3,4], [1,3,2,4]),
	([1,2,3,4,5], [1,5,2,4,3]),
])
def test_deck_revealed_increasing(deck, expected):
	solution = Solution()
	
	got = solution.deckRevealedIncreasing(deck)

	assert got == expected