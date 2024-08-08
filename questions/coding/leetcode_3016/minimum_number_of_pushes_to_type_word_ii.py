class Solution:
    def minimumPushes(self, word: str) -> int:
        total_presses = 0
        # Letter Frequency. (a=0...z=25)
        ltr_freq = [0] * 26
        for ltr in word:
            idx = ord(ltr) - 97
            ltr_freq[idx] += 1
        # Sort and filter out letters with frequency < 1
        ltr_freq.sort(reverse=True)
        while ltr_freq[-1] < 1:
            ltr_freq.pop()
        # Add  up button presses.
        for i in range(len(ltr_freq)):
            pressses = (i // 8) + 1 
            total_presses += ltr_freq[i] * pressses
        return total_presses