from typing import List
from collections import deque

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        output = deque([pairs[0]])
        idxs_used = [0] * len(pairs)
        idxs_used[0] = 1
        start_to_end = dict()
        end_to_start = dict()

        for i in range(len(pairs)):
            s, e = pairs[i]
            if s not in start_to_end:
                start_to_end[s] = dict()
            if e not in start_to_end[s]:
                start_to_end[s][e] = []
            start_to_end[s][e].append(i)
            if e not in end_to_start:
                end_to_start[e] = dict()
            if s not in end_to_start[e]:
                end_to_start[e][s] = []
            end_to_start[e][s].append(i)
        starts = ends = idx_count = 0
        for start, end_to_idxs in start_to_end.items():
            starts += 1
            for end, idxs in end_to_idxs.items():
                ends += 1
                idx_count += len(idxs)
        print(starts, ends, idx_count)
        starts = ends = idx_count = 0
        for start, end_to_idxs in end_to_start.items():
            starts += 1
            for end, idxs in end_to_idxs.items():
                ends += 1
                idx_count += len(idxs)
        print(starts, ends, idx_count)
        for i in range(len(pairs)):
            # Appending to end of output
            s = output[-1][-1]
            end_to_idx = start_to_end.get(s, dict())
            for end, idxs in end_to_idx.items():
                idx = 0
                while idxs:
                    idx = idxs.pop()
                    if idxs_used[idx]: continue
                if idxs_used[idx] == 0:
                    output.append([s,end])
                    idxs_used[idx] = 1
                    break
            # Appending to the front of output.
            e = output[0][0]
            start_to_idx = end_to_start.get(e, dict())
            for start, idxs in start_to_idx.items():
                idx = 0
                while idxs:
                    idx = idxs.pop()
                    if idxs_used[idx]: continue
                if idxs_used[idx] == 0:
                    output.appendleft([start,e])
                    idxs_used[idx] = 1
                    break
        
        return list(output)