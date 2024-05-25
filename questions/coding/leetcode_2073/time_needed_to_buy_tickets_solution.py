class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        # Attempt 1
        time = 0
        for i in range(len(tickets)):
            if i <= k:
                # Adding the min number of times we will have
                # to go through the time to get all our tickets
                time += min(tickets[i], tickets[k])
            else:
                # -1 is used here because these elements come AFTER k.
                # So this means that they will be seen tickets[k] - 1 times.
                time += min(tickets[i], tickets[k] - 1)
        return time
        # Attempt 0
        # time = 0
        # while True:
        #     for i in range(len(tickets)):
        #         if tickets[k] <= 0:
        #             return time
        #         if tickets[i] <= 0:
        #             continue
        #         time += 1
        #         tickets[i] -= 1