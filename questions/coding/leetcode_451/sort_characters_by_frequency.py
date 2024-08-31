class LetterFrequency:
    def __init__(self, ltr, frequency):
        self.ltr = ltr
        self.frequency = frequency

class Solution:
    def frequencySort(self, s: str) -> str:
        output = []
        ltr_freq_map = dict()
        for i in s:
            if i in ltr_freq_map:
                ltr_freq_map[i].frequency += 1
            else:
                ltr_freq_map[i] = LetterFrequency(ltr=i, frequency=1)
        
        ltr_freq_list = list(ltr_freq_map.values())
        ltr_freq_list.sort(key=lambda ltr_freq: ltr_freq.frequency, reverse=True)

        for ltr_freq in ltr_freq_list:
            for i in range(ltr_freq.frequency):
                output.append(ltr_freq.ltr)
        
        return ''.join(output)
