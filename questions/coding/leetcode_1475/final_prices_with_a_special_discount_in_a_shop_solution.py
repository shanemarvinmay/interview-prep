# TODO trace and implement this solution: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/solutions/685390/java-c-python-stack-one-pass/
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        final_prices = []

        for i in range(len(prices)):
            smaller_price = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    smaller_price = prices[j]
                    break
            final_prices.append(prices[i] - smaller_price)
        
        return final_prices