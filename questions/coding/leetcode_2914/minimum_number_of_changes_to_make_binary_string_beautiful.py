class Solution:
    def minChanges(self, s: str) -> int:
        diff = 0
        for i in range(1, len(s), 2):
            if s[i] != s[i-1]:
                diff += 1
        return diff

# Solution to what I thought the problem was.
# class Solution:
#     def minChanges(self, s: str) -> int:
#         sect_sz = self.get_sect_size(s)
#         sects = []
#         one_count = 0
#         for i, bit in enumerate(s):
#             if i > 0 and i % sect_sz == 0:
#                 sects.append(one_count)
#                 one_count = 0
#             if bit == '1':
#                 one_count += 1
#         sects.append(one_count)
#         diff = 0
#         for one_count in sects:
#             diff += min(one_count, sect_sz - one_count)
#         return diff
#     def get_sect_size(self, s):
#         n = len(s)
#         n = n / 2
#         while n > 1 and n % 2 != 0:
#             n = n / 2
#         if n <= 1:
#             return len(s)
#         return n
