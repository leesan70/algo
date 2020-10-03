from itertools import combinations_with_replacement
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def dfs(target, index, path):
            if target < 0:
                return
            if target == 0:
                results.append(path)
                return
            for i in range(index, len(candidates)):
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return results
