from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        curr_dist, max_dist = 0, 0
        curr_st, curr_end = None, None

        for i, seat in enumerate(seats):
            if seat == 0:
                if curr_st is None:
                    curr_st = i
                if curr_end is None:
                    curr_end = i
                else:
                    curr_end += 1

                curr_zeros = curr_end - curr_st + 1
                if curr_st == 0 or curr_end == len(seats) - 1:
                    curr_dist = curr_zeros
                else:
                    curr_dist = curr_zeros // 2 + 1 if curr_zeros % 2 == 1 else curr_zeros // 2

                if curr_dist > max_dist:
                    max_dist = curr_dist
            else:
                curr_st = None
                curr_end = None
        return max_dist
