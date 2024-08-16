class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        leafs = self.get_leafs(n)
        if k > leafs:
            return ''
        if k <= leafs/3:
            s = ['a']
            leafs /= 3
            self.helper(s, leafs, k, n)
        elif leafs/3 < k <= 2 * leafs/3:
            s = ['b']
            leafs /= 3
            k -= leafs
            self.helper(s,leafs , k, n)
        else:
            leafs /= 3
            k -= leafs * 2
            s = ['c']
            self.helper(s,leafs , k, n)
        return ''.join(s)
    def helper(self, s, leafs, k, n):
        if len(s) == n:
            return
        leafs //= 2
        if k <= leafs:
            # go left: take first letter
            ltrs = ['a','b','c']
        else:
            # go right: take last letter
            ltrs = ['c','b','a']
            k -= leafs
        for ltr in ltrs:
            if ltr != s[-1]:
                s.append(ltr)
                break
        self.helper(s, leafs, k, n)
    def get_leafs(self, n):
        if n == 1:
            return 3
        return 2 * self.get_leafs(n-1)
