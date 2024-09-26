from questions.coding.leetcode_1357.apply_discount_every_n_orders import Cashier

def test_cashier():
    cashier = Cashier(n=3,discount=50,products=[1,2,3,4,5,6,7],prices=[100,200,300,400,300,200,100])

    assert cashier.getBill([1,2],[1,2]) == 500

    assert cashier.getBill([3,7],[10,10]) == 4_000

    assert cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]) == 800

    assert cashier.getBill([4],[10]) == 4_000

    assert cashier.getBill([7,3],[10,10]) == 4_000

    assert cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]) == 7_350

    assert cashier.getBill([2,3,5],[5,3,2]) == 2_500

'''
Example 1:
Input
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
Output
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
Explanation
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // return 500.0. 1st customer, no discount.
                                                     // bill = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // return 4000.0. 2nd customer, no discount.
                                                     // bill = 10 * 300 + 10 * 100 = 4000.
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // return 800.0. 3rd customer, 50% discount.
                                                     // Original bill = 1600
                                                     // Actual bill = 1600 * ((100 - 50) / 100) = 800.
cashier.getBill([4],[10]);                           // return 4000.0. 4th customer, no discount.
cashier.getBill([7,3],[10,10]);                      // return 4000.0. 5th customer, no discount.
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // return 7350.0. 6th customer, 50% discount.
                                                     // Original bill = 14700, but with
                                                     // Actual bill = 14700 * ((100 - 50) / 100) = 7350.
cashier.getBill([2,3,5],[5,3,2]);                    // return 2500.0.  7th customer, no discount.
 

Constraints:
1 <= n <= 104
0 <= discount <= 100
1 <= products.length <= 200
prices.length == products.length
1 <= products[i] <= 200
1 <= prices[i] <= 1000
The elements in products are unique.
1 <= product.length <= products.length
amount.length == product.length
product[j] exists in products.
1 <= amount[j] <= 1000
The elements of product are unique.
At most 1000 calls will be made to getBill.
Answers within 10-5 of the actual value will be accepted.
'''
