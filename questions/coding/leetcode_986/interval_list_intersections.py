from typing import List

class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        ans = []
        fi = si = 0
        while fi < len(first) and si < len(second):
            # Finding ranges with overlap.
            while not self.has_overlap(first[fi], second[si]):
                if first[fi][1] < second[si][1]:
                    fi += 1
                else:
                    si += 1
                if fi >= len(first) or si >= len(second):
                    return ans
            # Appending intersection to answer.
            highest_low = max(first[fi][0], second[si][0])
            lowest_high = min(first[fi][1], second[si][1])
            ans.append([highest_low, lowest_high])

            # Inc lowest range
            if first[fi][1] == second[si][1] and second[si][1] == ans[-1][1]:
                if len(first) < len(second):
                    si += 1
                else:
                    fi += 1
            elif first[fi][1] == ans[-1][1] and first[fi][1] < second[si][1]:
                fi += 1
            else:
                si += 1

        return ans

    def has_overlap(self, first, second):
        partial_overlap = second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]
        second_fits_in_first = first[0] <= second[0] and second[1] <= first[1]
        first_fits_in_second = second[0] <= first[0] and first[1] <= second[1]
        return partial_overlap or second_fits_in_first or first_fits_in_second
