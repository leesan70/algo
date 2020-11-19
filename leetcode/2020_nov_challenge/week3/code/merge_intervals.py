from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for st, end in sorted(intervals):
            if not ans or ans[-1][1] < st:
                ans += [[st, end]]
            else:
                ans[-1][1] = max(ans[-1][1], end)
        return ans
