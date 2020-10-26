# Could not solve
# Solution https://leetcode.com/problems/stone-game-iv/solution/
# 1) DFS with memoization
from functools import lru_cache


class Solution:
    def winnerSquareGameDFS(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False

            sqrt_root = int(remain**0.5)
            for i in range(1, sqrt_root+1):
                # if there is any chance to make the opponent lose the game in the next round,
                #  then the current player will win.
                if not dfs(remain - i*i):
                    return True

            return False

        return dfs(n)

# 2) DP
    def winnerSquareGameDP(self, n: int) -> bool:
        dp = [False]*(n+1)
        for i in range(n+1):
            if dp[i]:
                continue
            for k in range(1, int(n**0.5)+1):
                if i+k*k <= n:
                    dp[i+k*k] = True
                else:
                    break
        return dp[n]
