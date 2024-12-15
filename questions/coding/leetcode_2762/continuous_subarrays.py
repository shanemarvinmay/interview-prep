from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        output = start = end = bg = sm = 0
        last_idx = -1

        def is_out_of_range(idx):
            return (abs(nums[idx] - nums[bg]) > 2 or 
                    abs(nums[idx] - nums[sm]) > 2)

        while end < len(nums):
            if is_out_of_range(end):
                # Capturing the subs
                if start <= last_idx:
                    overlap = max(last_idx - (start-1), 1)
                    output -= (overlap*(overlap + 1)) / 2
                last_idx = end - 1
                n = end - start
                output += (n*(n + 1)) / 2
                while is_out_of_range(end):
                    start += 1
                    bg = max(bg, start)
                    if nums[end] > nums[bg]: bg = end
                    sm = max(sm, start)
                    if nums[end] < nums[sm]: sm = end
                
            if nums[end] > nums[bg]: bg = end
            if nums[end] < nums[sm]: sm = end

            end += 1
            
        if start <= last_idx:
            overlap = max(last_idx - (start-1), 1)
            output -= (overlap*(overlap + 1)) / 2
        n = end - start
        output += (n*(n + 1)) / 2

        return output
