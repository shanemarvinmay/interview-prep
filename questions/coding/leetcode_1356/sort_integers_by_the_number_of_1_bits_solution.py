class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort()

        # Get binary 1s count and zip them in the list
        i = 0
        while i < len(arr):
            binary = bin(arr[i])
            ones = binary.count('1')
            arr[i] = [arr[i], ones]
            i += 1

        # Sort based on 1s
        arr = sorted(arr, key=lambda x: x[1])
        
        # return numbers
        return [num for num, _ in arr]