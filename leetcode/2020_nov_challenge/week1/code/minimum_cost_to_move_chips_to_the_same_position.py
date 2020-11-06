from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd_sum, even_sum = 0, 0
        for pos in position:
            if pos % 2 == 0:
                even_sum += 1
            else:
                odd_sum += 1
        return min(even_sum, odd_sum)
