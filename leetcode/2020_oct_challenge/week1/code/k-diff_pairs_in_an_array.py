from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        c = Counter(nums)
        for num in c:
            if k == 0:
                if c[num] >= 2:
                    count += 1
            else:
                if num - k in c:
                    count += 1
        return count
