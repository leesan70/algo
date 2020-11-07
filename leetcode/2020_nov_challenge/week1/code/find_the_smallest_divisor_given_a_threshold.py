import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        st, end = 1, max(nums)
        sol = None
        while st <= end:
            mid = (st + end) // 2
            eval_ = sum(map(lambda num: math.ceil(num / mid), nums))
            if eval_ <= threshold:
                sol = mid
                end = mid - 1
            else:
                st = mid + 1
        return sol
