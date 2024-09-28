class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        '''
        sum s sub freq * sum t sub freq if len match and only one char diff.'''
        total = 0
        # get subs_freq maps
        s_sub_freq = self.get_sub_freq_map(s)
        t_sub_freq = self.get_sub_freq_map(t)
        # loop thr and count one offs
        for s_sub, s_freq in s_sub_freq.items():
            for t_sub, t_freq in t_sub_freq.items():
                if len(s_sub) == len(t_sub) and self.is_one_diff(s_sub, t_sub):
                    total += s_freq * t_freq
        return total
    def get_sub_freq_map(self, s):
        sub_freq = dict()
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub not in sub_freq:
                    sub_freq[sub] = 0
                sub_freq[sub] += 1
        return sub_freq
    def is_one_diff(self, s, t):
        one_diff = False
        for i in range(len(s)):
            if s[i] != t[i]:
                if one_diff:
                    return False
                one_diff = True
        return one_diff
