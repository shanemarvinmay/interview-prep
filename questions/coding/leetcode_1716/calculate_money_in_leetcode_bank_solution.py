class Solution:
    def totalMoney(self, n: int) -> int:
        # This is a better solution.
        # implement this https://leetcode.com/problems/calculate-money-in-leetcode-bank/solutions/4367675/o-1-math-explained/
        weeks = n // 7
        money = weeks * 28
        money += (7 * weeks * (weeks - 1)) // 2

        # Calculating the extra days that didn't make a whole week.
        if n % 7:
            extra_days = n % 7
            money_to_add = weeks + 1
            for i in range(extra_days):
                money += money_to_add
                money_to_add += 1

        # Attempt 0
        # money = 0
        # amount_deposited = 1
        # for i in range(1, n + 1):
        #     money += amount_deposited
        #     if i % 7 == 0:
        #         amount_deposited -= 5
        #     else:
        #         amount_deposited += 1
                
        return money