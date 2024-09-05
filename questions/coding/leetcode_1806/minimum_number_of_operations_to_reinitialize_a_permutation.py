class Solution:
    def reinitializePermutation(self, n: int) -> int:
        operation_count = 0
        i = 1
        while i != 1 or operation_count == 0:
            if i % 2:
                i = (n + i - 1) / 2
            else:
                i = i / 2
            operation_count += 1
        return operation_count
        