class Solution:
    def get_sum_of_digits(self, x):
        total = 0
        
        while x:
            total += x % 10
            x //= 10
        
        return total

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        # get sum of digits
        sum_of_digits = self.get_sum_of_digits(x)

        # deterin if harshad num (x % sum == 0)
        if x % sum_of_digits:
            return -1
        return sum_of_digits