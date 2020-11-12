import itertools
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def D(comb):
            P, Q = comb
            return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2
        S = set(map(D, itertools.combinations((p1, p2, p3, p4), 2)))
        return len(S) == 2 and 0 not in S
