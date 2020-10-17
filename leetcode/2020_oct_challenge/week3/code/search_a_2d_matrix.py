from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary Search on 2D list
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        outer_st = 0
        outer_end = len(matrix) - 1
        while outer_st <= outer_end:
            outer_mid = (outer_st + outer_end) // 2
            if matrix[outer_mid][0] <= target <= matrix[outer_mid][-1]:
                inner_st = 0
                inner_end = len(matrix[outer_mid]) - 1
                while inner_st <= inner_end:
                    inner_mid = (inner_st + inner_end) // 2
                    if target == matrix[outer_mid][inner_mid]:
                        return True
                    elif target > matrix[outer_mid][inner_mid]:
                        inner_st = inner_mid + 1
                    else:
                        inner_end = inner_mid - 1
                return False
            elif target > matrix[outer_mid][-1]:
                outer_st = outer_mid + 1
            elif target < matrix[outer_mid][0]:
                outer_end = outer_mid - 1
        return False
