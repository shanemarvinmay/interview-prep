from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = []
        counter = Counter(s)
        # Putting the ordered letters first.
        for ltr in order:
            freq = counter.get(ltr, 0)
            for _ in range(freq):
                output.append(ltr)
        # Now for the rest of the letters.
        for ltr, freq in counter.items():
            if ltr in order: continue
            for _ in range(freq):
                output.append(ltr)
        return ''.join(output)
