from collections import deque
class Solution:
    def turn_int_to_digit_list(self, num: int) -> list[int]:
        '''Takes in a digit and returns a list of the digits.'''
        q = deque()
        while num:
            last_digit = num % 10
            q.appendleft(last_digit)
            num = num // 10
        return list(q)
    
    def separateDigits(self, nums: list[int]) -> list[int]:
        digits = []

        for num in nums:
            digits.extend(self.turn_int_to_digit_list(num))

        return digits
        