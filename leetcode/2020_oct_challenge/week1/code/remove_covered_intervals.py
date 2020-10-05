from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort on increasing start time and decreasing end time
        intervals.sort(key = lambda x:(x[0], -x[1]))
        last = -1
        removed = 0
        # If end time of an interval is smaller than the last, this one is covered
        # because any interval to the left has smaller start time due to sorting
        for i in intervals:
            if i[1] <= last:
                removed += 1
            else:
                last = i[1]
        return len(intervals) - removed
