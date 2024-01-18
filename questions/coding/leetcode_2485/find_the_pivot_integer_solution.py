class Solution:
    def pivotInteger(self, n: int) -> int:
        # Attempt 0 Time:O(n)
        # high = higher_sum = n
        # low = lower_sum = 1
        
        # while low != high:
        #     print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
        #     if lower_sum < higher_sum:
        #         low += 1
        #         lower_sum += low
        #         print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
        #     else:
        #         high -= 1
        #         higher_sum += high
        #         print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')

        # print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
        # if lower_sum == higher_sum:
        #     return high # could also be low
        # return -1
        
        # Attempt 1 O(log(n))
        n_summation = n * (n + 1) / 2
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2

            if mid * mid == n_summation:
                return mid
            elif mid * mid > n_summation:
                r = mid
            else:
                l = mid + 1
        
        if l * l == n_summation:
            return l
        return -1

