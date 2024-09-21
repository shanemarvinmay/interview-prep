class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        n = len(num)
        # Finding kth permutation.
        perm = list(num)
        for _ in range(k):
            self.get_next_permutation(perm)
        # Counting the differences.
        swaps = 0
        num = list(num)
        for i in range(n):
            j = i
            # Finding where perm[i] is in the num.
            while j < n and perm[i] != num[j]:
                j += 1
            # Adding the distance (num of swaps) needed to restore num.
            swaps += j - i
            # Moving j up to simulate swaps.
            num[i:j+1] = [num[j]] + num[i:j]
        return swaps
        
    def get_next_permutation(self, num: list) -> str:
        n = len(num)
        # Find first number that is smaller than the one that comes after.
        i = n - 1
        while i > 0 and num[i-1] >= num[i]:
            i -= 1
        # Find either last num or a number smaller that than the one we found earlier.
        j = i
        while j < n and num[i-1] < num[j]:
            j += 1
        num[i-1], num[j-1] = num[j-1], num[i-1]
        num[i:] = num[i:][::-1]
        return num
