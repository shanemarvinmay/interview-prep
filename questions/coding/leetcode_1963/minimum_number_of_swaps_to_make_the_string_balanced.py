class Solution:
    def minSwaps(self, s: str) -> int:
        problems = 0
        opens = 0
        for i in s:
            if i == '[':
                opens += 1
            else:
                if opens:
                    opens -= 1
                else:
                    problems += 1
            
        return (problems + 1) // 2
