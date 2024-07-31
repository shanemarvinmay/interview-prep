class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        output = []
        matrix = self.build_sorted_matrix(s1, s2)
        for row in matrix:
            print(row)
        for i in range(len(baseStr)):
            output.append(baseStr[i])
            # Finding the smallest letter.
            for row in matrix:
                if output[i] in row:
                    output[i] = row[0]
                    break
        
        return ''.join(output)

    def build_sorted_matrix(self, s1, s2):
        matrix = []

        for i in range(len(s1)):
            ltrs_placed = False
            for row in matrix:
                if s1[i] in row or s2[i] in row:
                    if s1[i] in ['a', 'b'] or s2[i] in ['a', 'b']:
                        print(f'{s1[i]} {s2[i]} are being placed in {row}')
                    ltrs_placed = True
                    row.add(s1[i])
                    row.add(s2[i])
                    break
            if not ltrs_placed:
                if s1[i] in ['a', 'b'] or s2[i] in ['a', 'b']:
                    print(f'{s1[i]} {s2[i]} are being placed in a new row')
                matrix.append(set([s1[i], s2[i]]))
        
        i = 0
        while i < len(matrix):
            j = i + 1
            while j < len(matrix):
                common = matrix[i].intersection(matrix[j])
                if common:
                    for k in matrix[j]:
                        matrix[i].add(k)
                    del matrix[j]
                else:
                    j += 1
            i += 1
        
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])
        
        for i in range(len(matrix)):
            matrix[i].sort()
        
        return matrix