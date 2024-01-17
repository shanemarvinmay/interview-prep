class Solution:
    def numberOfBeams(self, bank):
        beams = 0
        prev = 0

        for row in bank:
            cur = row.count('1')
            if prev:
                beams += prev * cur
            if cur:
                prev = cur

        return beams