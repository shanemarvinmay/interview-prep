class Solution:
    def merge_sort(self, scores, k):
        if len(scores) < 2:
            return

        mid = len(scores) // 2
        left = scores[:mid]
        right = scores[mid:]
        self.merge_sort(left, k)
        self.merge_sort(right, k)

        left_idx, right_idx, scores_idx = 0, 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx][k] > right[right_idx][k]:
                scores[scores_idx] = left[left_idx]
                left_idx += 1
            else:
                scores[scores_idx] = right[right_idx]
                right_idx += 1
            scores_idx += 1
        
        while left_idx < len(left):
            scores[scores_idx] = left[left_idx]
            left_idx += 1
            scores_idx += 1
        
        while right_idx < len(right):
            scores[scores_idx] = right[right_idx]
            right_idx += 1
            scores_idx += 1
        

    def sortTheStudents(self, scores: list[list[int]], k: int) -> list[list[int]]:
        self.merge_sort(scores, k)
        return scores
        