from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        # Sort on increasing start time and increasing end time
        points.sort(key = lambda x:(x[0], x[1]))
        reference = points[0]
        overlap = 0
        for pt in points[1:]:
            if reference[0] <= pt[0] <= reference[1]:
                overlap += 1
                # Keep on shrinking the size of the intervals
                reference[0] = max(pt[0], reference[0])
                reference[1] = min(pt[1], reference[1])
            else:
                reference = pt
        return len(points) - overlap
