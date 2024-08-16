from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        till = {5:0, 10:0, 20:0}
        for bill in bills:
            # Inc bill count.
            till[bill] += 1
            # Give change
            change = bill - 5
            if self.get_change(till, change) == False:
                return False
        return True
    def get_change(self, till, change):
        bills = [5, 10]
        while len(bills):
            bill = bills.pop()
            while till[bill] > 0 and change >= bill:
                change -= bill
                till[bill] -= 1
            if change == 0:
                return True
        return False


        