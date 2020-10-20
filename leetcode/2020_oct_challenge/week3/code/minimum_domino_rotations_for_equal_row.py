# My implementation below was a bit slow
# Reference for faster implementation
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC%2B%2BPython-Different-Ideas
from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        num_swaps_to_A = [0 for _ in range(6)]
        num_swaps_to_B = [0 for _ in range(6)]
        for a, b in zip(A, B):
            for i in range(6):
                if num_swaps_to_A[i] >= 0 and num_swaps_to_B[i] >= 0:
                    if a == i + 1 or b == i + 1:
                        num_swaps_to_A[i] += 0 if a == i + 1 else 1
                        num_swaps_to_B[i] += 0 if b == i + 1 else 1
                    else:
                        num_swaps_to_A[i] = -1
                        num_swaps_to_B[i] = -1

        min_swap = -1
        num_swaps_to_A = filter(lambda a: a >= 0, num_swaps_to_A)
        num_swaps_to_B = filter(lambda b: b >= 0, num_swaps_to_B)

        for a, b in zip(num_swaps_to_A, num_swaps_to_B):
            min_swap = min(min_swap, a, b) if min_swap >= 0 else min(a, b)
        return min_swap