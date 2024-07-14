class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        cur_sub = set()

        for ltr in s:
            if ltr in cur_sub:
                count += 1
                cur_sub = set()
            cur_sub.add(ltr)
        
        return count
