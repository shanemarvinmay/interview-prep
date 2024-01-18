class Solution:
    def pivotInteger(self, n: int) -> int:
        high = higher_sum = n
        low = lower_sum = 1
        
        while low != high:
            print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
            if lower_sum < higher_sum:
                low += 1
                lower_sum += low
                print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
            else:
                high -= 1
                higher_sum += high
                print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')

        print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
        if lower_sum == higher_sum:
            return high # could also be low
        return -1
