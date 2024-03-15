class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        end_of_trailing_zeros = len(num)

        for i in range(len(num) - 1, 0, -1):
            if num[i] == '0':
                end_of_trailing_zeros = i
            else:
                break

        return ''.join(num[:end_of_trailing_zeros])
