from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        time_poisoned = 0
        for i in range(len(timeSeries)):
            if i < len(timeSeries) - 1:
                time_poisoned += min(timeSeries[i + 1] - timeSeries[i], duration)
            else:
                time_poisoned += duration
        return time_poisoned
