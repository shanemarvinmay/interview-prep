from math import ceil

class Solution:
    def merge_sort(self, piles):
        if len(piles) < 2:
            return
        
        mid = len(piles) // 2
        left = piles[:mid]
        right = piles[mid:]
        self.merge_sort(left)
        self.merge_sort(right)

        left_idx, right_idx, piles_idx = 0, 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] > right[right_idx]:
                piles[piles_idx] = left[left_idx]
                left_idx += 1
            else:
                piles[piles_idx] = right[right_idx]
                right_idx += 1
            piles_idx += 1

        while left_idx < len(left):
            piles[piles_idx] = left[left_idx]
            left_idx += 1
            piles_idx += 1
        while right_idx < len(right):
            piles[piles_idx] = right[right_idx]
            right_idx += 1
            piles_idx += 1

    def maxCoins(self, piles: list[int]) -> int:
        # Attempt 1 Time O(n)
        my_coins = 0
        turns = len(piles) / 3
        add = False
        max_value = max(piles)
        freq = [0] * (max_value + 1)

        for pile in piles:
            freq[pile] += 1

        i = max_value
        while turns:
            # Finding next pile
            while freq[i] == 0:
                i -= 1
            if add:
                my_coins += i
                turns -= 1
                add = False
            else:
                add = True
            freq[i] -= 1

        return my_coins
        # Attempt 0 Time O(nlog(n))
        # max_coins = 0
        # # Sorting in descending order (biggest to smallest).
        # self.merge_sort(piles)
        # # Looping the the largest 2/3 nums and adding every other one
        # two_thirds = ceil(len(piles) * 2 / 3)
        # # Starting at 1 because 0 is the largest and Alice will get it.
        # # two_thirds + 1 because we want to include the num at index two_thirds.
        # # We are stepping by 2 because Alice gets the others.
        # for i in range(1, two_thirds + 1, 2):
        #     max_coins += piles[i]
    
        # return max_coins