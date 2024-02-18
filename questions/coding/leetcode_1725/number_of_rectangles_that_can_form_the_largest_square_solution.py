class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        max_len = 0
        largest_square_count = 0

        for rectangle_sides in rectangles:
            current_square_length = min(rectangle_sides)
            if current_square_length > max_len:
                largest_square_count = 1
                max_len = current_square_length
            elif current_square_length == max_len:
                largest_square_count += 1

        return largest_square_count