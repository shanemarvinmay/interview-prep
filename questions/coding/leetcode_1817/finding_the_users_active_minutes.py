from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        output = [0] * k
        usr_to_mins = dict()

        for log in logs:
            uid = log[0]
            time = log[1]
            if log[0] not in usr_to_mins:
                usr_to_mins[uid] = set()
            usr_to_mins[uid].add(time)

        for _, mins in usr_to_mins.items():
            num_min = len(mins)
            output[num_min - 1] += 1
        
        return output