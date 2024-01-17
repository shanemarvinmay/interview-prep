class Solution:
    def pivotInteger(self, n: int) -> int:
        high = higher_sum = n
        low = lower_sum = 1
        
        while low < high and lower_sum != higher_sum or lower_sum == 0:
            print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
            while lower_sum < higher_sum:
                low += 1
                lower_sum += low
                print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
            while lower_sum > higher_sum:
                high -= 1
                higher_sum += high
                print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')

        print(f'lower_sum:{lower_sum}\tlow:{low}\thigher_sum:{higher_sum}\thigh:{high}')
        middle = (high + low) / 2
        if lower_sum == higher_sum and middle == round(middle):
            return middle
        return -1
