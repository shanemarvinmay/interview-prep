from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cur_time = 0
        wait_times = []
        for customer in customers:
            arrival, wait = customer
            cur_time = max(cur_time, arrival)
            cur_time += wait
            wait_times.append(cur_time - arrival)
        return sum(wait_times) / len(wait_times)
