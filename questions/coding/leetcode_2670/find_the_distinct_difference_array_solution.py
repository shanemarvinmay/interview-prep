from collections import Counter
from typing import List

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        seen = set()
        unseen = Counter(nums)

        for i in range(len(nums)):
            num = nums[i]
            seen.add(num)

            # Updating unique unseen numbers.
            unseen[num] -= 1
            # Removing the number if there are no more unseen.
            # In other words, remove the number if we've seen 
            # every time it occures.
            if unseen[num] < 1:
                del unseen[num]
            
            nums[i] = len(seen) - len(unseen.keys())
        
        return nums
