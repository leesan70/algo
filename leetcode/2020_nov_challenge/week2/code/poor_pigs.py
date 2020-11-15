from math import log

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num_pigs = 0
        # better to compute log than computing power
        # Find minimum x such that (T+1)^x >= N
        # while (minutesToTest / minutesToDie + 1) ** num_pigs < buckets):
        while num_pigs < log(buckets) / log(minutesToTest / minutesToDie + 1):
            num_pigs += 1
        return num_pigs
