class Solution:
    def pivotArray(self, nums, pivot):
        # Time O(n) Space O(n)
        output = []
        for num in nums:
            if num < pivot:
                output.append(num)
        for num in nums:
            if num == pivot:
                output.append(num)
        for num in nums:
            if num > pivot:
                output.append(num)
        return output
    
        # # Time O(n^2) Space O(1)
        # # Getting the nums < pivot on the left side
        # for i in range(len(nums)):
        #     if nums[i] > pivot:
        #         # Finding next num that is < pivot
        #         less = i+1
        #         while less < len(nums):
        #             if nums[less] < pivot:
        #                 break
        #             less += 1
        #         # No following nums < pivot
        #         if less >= len(nums):
        #             break
        #         # Swap
        #         nums[i], nums[less] = nums[less], nums[i]
        # # Getting the nums == pivot in the middle
        # for i in range(len(nums)):
        #     if nums[i] > pivot:
        #         # Finding the next num == pivot
        #         equals = i + 1
        #         while equals < len(nums):
        #             if nums[equals] == pivot:
        #                 break
        #             equals += 1
        #         # No following nums == p
        #         if equals >= len(nums):
        #             break
        #         # Swap
        #         nums[i], nums[equals] = nums[equals], nums[i]
        
        # return nums
