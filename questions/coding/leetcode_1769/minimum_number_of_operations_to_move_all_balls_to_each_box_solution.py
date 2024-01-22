class Solution:
    def min_operations(self, boxes: str) -> list[int]:
        # Attempt 0 O(n^2)
        # output = []

        # # Getting index of 1s.
        # one_idxs = set()
        # for i in range(len(boxes)):
        #     if boxes[i] == '1':
        #         one_idxs.add(i)
        
        # # Calculating moves.
        # for i in range(len(boxes)):
        #     moves = 0
        #     for idx in one_idxs:
        #         moves += abs(idx - i)
        #     output.append(moves)
        
        # return output

        # Attempt 1 O(n)
        output = []
        # Calc how many moves each box cost (from the left)
        left_count, left_cost = 0, 0
        for i in range(len(boxes)):
            output.append(left_cost)
            if boxes[i] == '1':
                left_count += 1
            left_cost += left_count
        print(output)
        # Calc how many moves each box cost (from the right)
        right_count, right_cost = 0, 0
        for i in range(len(boxes) - 1, -1, -1):
            output[i] += right_cost
            if boxes[i] == '1':
                right_count += 1
            right_cost += right_count
        return output