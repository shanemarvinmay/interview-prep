class Solution:
    def minFlips(self, target: str) -> int:
        flip_count = 0
        status = '0'
        for bit in target:
            if bit != status:
                status = '0' if status == '1' else '1'
                flip_count += 1
        return flip_count
