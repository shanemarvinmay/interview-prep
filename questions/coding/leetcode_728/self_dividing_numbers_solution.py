class Solution:

    def get_digits(self, num):
        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        return digits
    
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        self_dividing_numbers = []

        for num in range(left, right + 1):

            if num < 10:
                self_dividing_numbers.append(num)
                continue

            digits = self.get_digits(num)
            
            non_divisible_digits = [digit for digit in digits if digit == 0 or num % digit != 0]
            if len(non_divisible_digits) == 0:
                self_dividing_numbers.append(num)

        return self_dividing_numbers
        