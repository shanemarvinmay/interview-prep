class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        highest_odd = []

        # Counting ones and zeros
        ones, zeros = 0, 0
        for char in s:
            if char == '1':
                ones += 1
            else:
                zeros += 1

        # Place all but one one up front.
        for _ in range(ones - 1):
            highest_odd.append('1')
        # Appending all zeros
        for _ in range(zeros):
            highest_odd.append('0')
        # Appending the last one so the number is odd
        highest_odd.append('1')

        return ''.join(highest_odd)