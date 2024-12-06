class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        sstack, tstack = [], []
        for i in range(n):
            if start[i] in ['L','R']:
                sstack.append((start[i], i))
            if target[i] in ['L','R']:
                tstack.append((target[i], i))
        if len(sstack) != len(tstack): return False
        while sstack:
            sltr, spos = sstack.pop()
            tltr, tpos = tstack.pop()
            if sltr != tltr: return False
            # Rs from start cannot be right of the same R in target
            # Because that implies the R went left
            if sltr == 'R' and spos > tpos: return False
            # Vice versa for Ls
            if sltr == 'L' and spos < tpos: return False
        return True
