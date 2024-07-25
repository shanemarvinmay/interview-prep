class Solution:
    def removeStars(self, s: str) -> str:
        del_idxs = set()
        del_ltrs = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '*':
                del_ltrs += 1
                del_idxs.add(i)
            elif s[i].isalpha() and del_ltrs:
                del_ltrs -= 1
                del_idxs.add(i)
        
        return ''.join([s[i] for i in range(len(s)) if i not in del_idxs])
