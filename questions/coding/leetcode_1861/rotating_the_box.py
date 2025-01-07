from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Sliding all stones to the right
        ROWS, COLS = len(box), len(box[0])
        for row in range(ROWS):
            free_space = COLS - 1
            col = free_space
            while col > -1 and free_space > -1:
                # Finding first free space
                while free_space > -1  and box[row][free_space] != '.':
                    free_space -= 1
                # Finding next obsticle or stone
                col = free_space - 1
                while col > -1 and box[row][col] not in ['*', '#']:
                    col -= 1

                if col < 0:
                    break
                elif box[row][col] == '*':
                    free_space = col
                else:
                    box[row][col], box[row][free_space] = box[row][free_space], box[row][col]

                free_space -= 1
                
        res = []
        for col in range(len(box[0])):
            res.append(['.' for _ in range(len(box))])
        
        res_col = ROWS - 1
        for row in range(len(box)):
            for col in range(len(box[0])):
                res[col][res_col] = box[row][col]
            res_col -= 1

        return res
        # res = []
        # for col in range(len(boxGrid[0])):
        #     res.append(['.' for _ in range(len(boxGrid))])
        
        # res_col = len(boxGrid) - 1
        # for row in range(len(boxGrid)):
        #     for col in range(len(boxGrid[0])):
        #         res[col][res_col] = boxGrid[row][col]
        #     res_col -= 1
        
        # # falling stones from bottom up
        # # col by col
        # COLS = len(res[0])
        # ROWS = len(res)
        # for col in range(COLS):
        #     stone = ROWS - 1
        #     # find first stone
        #     while stone > -1:
        #         while stone > -1 and res[stone][col] != '#':
        #             stone -= 1
            
        #         # find where stops
        #         stop = stone + 1
        #         while stop < ROWS and res[stop][col] == '.':
        #             stop += 1
        #         stop -= 1

        #         # swap 'em
        #         res[stone][col], res[stop][col] = res[stop][col], res[stone][col]
        #         stone -= 1
            
        # return res
