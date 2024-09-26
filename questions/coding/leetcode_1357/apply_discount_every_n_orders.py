from typing import List

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer_count = 1
        self.n = n
        self.discount = discount
        self.product_price = dict()
        for i in range(len(products)):
            product = products[i]
            price = prices[i]
            self.product_price[product] = price

    def getBill(self, products: List[int], amounts: List[int]) -> float:
        total = 0
        for i in range(len(products)):
            product_id = products[i]
            total += self.product_price[product_id] * amounts[i]
        
        if self.customer_count == self.n:
            self.customer_count = 0
            total = total * ((100 - self.discount) / 100)
        self.customer_count += 1

        return total
