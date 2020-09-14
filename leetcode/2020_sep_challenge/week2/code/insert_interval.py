from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        startIndex = None
        startPassed = False
        endIndex = None
        endPassed = False

        for i in range(len(intervals)):
            if startIndex is None:
                if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                    startIndex = i
                elif newInterval[0] < intervals[i][0]:
                    startIndex = i
                    startPassed = True
            if startIndex is not None and endIndex is None:
                if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                    endIndex = i
                elif newInterval[1] < intervals[i][0]:
                    endIndex = i
                    endPassed = True
            if startIndex is not None and endIndex is not None:
                break
        if startIndex is None:
            intervals.append(newInterval)
            return intervals
        if endIndex is None:
            endPassed = True
            endIndex = len(intervals)

        # print(startIndex, endIndex, startPassed, endPassed)
        if startPassed and endPassed:
            intervals = intervals[0:startIndex] + [newInterval] + intervals[endIndex:]
        elif startPassed:
            new = [newInterval[0], intervals[endIndex][1]]
            # merge
            intervals = intervals[0:startIndex] + [new] + intervals[endIndex + 1:]
        elif endPassed:
            new = [intervals[startIndex][0], newInterval[1]]
            # merge
            intervals = intervals[0:startIndex] + [new] + intervals[endIndex:]
        else:
            new = [intervals[startIndex][0], intervals[endIndex][1]]
            # merge
            intervals = intervals[0:startIndex] + [new] + intervals[endIndex + 1:]
        return intervals
