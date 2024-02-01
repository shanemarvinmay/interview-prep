class Solution:
    def brute_force(self, start, end, nums):
        sorted_subarray = sorted(nums[start:end+1])
        diff = sorted_subarray[1] - sorted_subarray[0]
        for i in range(1, len(sorted_subarray)):
            if sorted_subarray[i] - sorted_subarray[i-1] != diff:
                return False
        return True
    
    def is_arithmetic_sequence(self, start, end, nums):
        unique_nums = set()
        # Finding the biggest and smallest element between start and end.
        # This will be used to find the difference that should be between every number.
        biggest = smallest = nums[start]
        for i in range(start, end + 1):
            unique_nums.add(nums[i])
            biggest = max(biggest, nums[i])
            smallest = min(smallest, nums[i])
        # Finding the expected uniform difference between all numbers (as mentioned above)
        diff = (biggest - smallest) / (end - start)
        # Since every number is an int, if diff isn't, then we know this can't be an arithmetic sequence.
        if diff != round(diff):
            return False
        # Counting up from the smallest number to the biggest number. Adding the expected diff every time.
        for i in range(end - start + 1):
            target_num = smallest + i * diff
            if target_num not in unique_nums:
                return False
        return True
    
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        answers = []

        for i in range(len(l)):
            answer = self.is_arithmetic_sequence(start=l[i], end=r[i], nums=nums)
            # answer = self.brute_force(start=l[i], end=r[i], nums=nums)
            answers.append(answer)

        return answers
