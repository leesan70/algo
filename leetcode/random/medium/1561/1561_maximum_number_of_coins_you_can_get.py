from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_ = sorted(piles)
        sum_ = 0
        for i in range(len(sorted_)//3):
            sum_ += sorted_[len(sorted_) - 2 * i - 2]
        return sum_
