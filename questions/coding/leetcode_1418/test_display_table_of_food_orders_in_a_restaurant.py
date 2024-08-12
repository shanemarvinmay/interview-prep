from questions.coding.leetcode_1418.display_table_of_food_orders_in_a_restaurant import Solution

import pytest


@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('orders, expected', [
    ([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]],
     [
        ["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
        ["3","0","2","1","0"],
        ["5","0","1","0","1"],
        ["10","1","0","0","0"]
    ]),
    ([["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]],
     [
        ["Table","Canadian Waffles","Fried Chicken"],
        ["1","2","0"],
        ["12","0","3"]
    ]),
    ([["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]],
     [
        ["Table","Bean Burrito","Beef Burrito","Soda"],
        ["2","1","1","1"]
    ])
])
def test_displayTable(orders, expected, sol):
    got = sol.displayTable(orders)

    assert got == expected