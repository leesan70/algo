# Could not solve
# Solution https://leetcode.com/problems/minimum-height-trees/discuss/76132/Iterative-remove-leaves-Python-solution
import collections
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        d = collections.defaultdict(set)
        for u, v in edges:
            d[u].add(v)
            d[v].add(u)
        s = set(range(n))
        while len(s) > 2:
            leaves = set(i for i in s if len(d[i]) == 1)
            s -= leaves
            for i in leaves:
                for j in d[i]:
                    d[j].remove(i)
        return list(s)