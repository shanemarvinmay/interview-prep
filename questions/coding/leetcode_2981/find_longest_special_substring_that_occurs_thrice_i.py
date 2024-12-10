class Solution:
    def maximumLength(self, s: str) -> int:
        # {sub: {freq:#, length:#}}
        hm = dict()
        n = len(s)
        i  = 0
        while i < n:
            ltr = s[i]
            count = 0
            while i < n and s[i] == ltr:
                i += 1
                count += 1
            j = 0
            while j < count:
                length = j + 1
                sub = f'{ltr}:{length}'
                if sub not in hm:
                    hm[sub] = {'freq': 0, 'length':length}
                hm[sub]['freq'] += count - j
                j += 1
        
        max_length = -1
        for sub in hm:
            if hm[sub]['freq'] < 3: continue
            max_length = max(max_length, hm[sub]['length'])
        
        return max_length
