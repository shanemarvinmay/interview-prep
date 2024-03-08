class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        num_to_freq = [0] * 101

        for num in nums:
            num_to_freq[num] += 1
        
        max = 0
        max_freq = 1
        for freq in num_to_freq:
            if freq == 0:
                continue
            if freq == max:
                max_freq += 1
            elif freq > max:
                max = freq
                max_freq = 1
        
        return max * max_freq