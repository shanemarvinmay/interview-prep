class Solution:
    def sortVowels(self, s: str) -> str:
        ltrs = list(s)

        vowels = []
        LIST_OF_VOWELS = ['A','E','I','O','U','a','e','i','o','u']
        for i in range(len(ltrs)):
            if ltrs[i] in LIST_OF_VOWELS:
                vowels.append(ltrs[i])
                ltrs[i] = None
        
        vowels.sort(reverse=True)

        for i in range(len(ltrs)):
            if ltrs[i] is None:
                ltrs[i] = vowels.pop()
        
        return ''.join(ltrs)