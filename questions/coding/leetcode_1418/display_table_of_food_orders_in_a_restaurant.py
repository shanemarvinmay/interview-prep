from typing import List

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        # { table_num : {food_name: qty}}
        table_map = dict()
        # This will be used to get alphabetical order later.
        foods = set()
        tables = set()

        for order in orders:
            # Storing order in map.
            _, table_num, food = order
            if table_num not in table_map:
                table_map[table_num] = dict()
            if food not in table_map[table_num]:
                table_map[table_num][food] = 0
            table_map[table_num][food] += 1
            # Saving tables and food in food list.
            foods.add(food)
            tables.add(int(table_num))
        
        # Creating table
        header = ['Table']
        foods = list(foods)
        foods.sort()
        header.extend(foods)
        table = [header]
        tables = list(tables)
        tables.sort()
        for table_num in tables:
            table_num = f'{table_num}'
            row = [table_num]
            for food in foods:
                qty = table_map[table_num].get(food, 0)
                row.append(f'{qty}')
            table.append(row)

        return table

'''
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito". 
Example 2:
Input: orders = 
Output: 

Explanation: 
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".
Example 3:
Input: orders = 
Output: 

Constraints:
1 <= orders.length <= 5 * 10^4
orders[i].length == 3
1 <= customerNamei.length, foodItemi.length <= 20
customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
tableNumberi is a valid integer between 1 and 500.
'''