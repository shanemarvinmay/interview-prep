from typing import List

class Solution:
    def xorQueries(self, ar: List[int], queries: List[List[int]]) -> List[int]:
        self.ar = ar
        # Getting list of xors.
        self.xors = self.get_xors(ar)
        # Executing queries.
        results = []
        for query in queries:
            result = self.execute_query(query)
            results.append(result)
        return results
    def execute_query(self, query):
        start, end = query
        if start == end:
            return self.ar[start]
        elif start == 0:
            return self.xors[end]
        else:
            return self.xors[start-1] ^ self.xors[end]
    def get_xors(self, ar):
        xors = []
        xor = 0
        for num in ar:
            xor ^= num
            xors.append(xor)
        
        return xors
