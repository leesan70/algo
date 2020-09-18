from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = -1e10, 1e10
        for p in prices:
            min_price = min(min_price, p)
            profit = p - min_price
            max_profit = max(max_profit, profit)
        return max_profit
