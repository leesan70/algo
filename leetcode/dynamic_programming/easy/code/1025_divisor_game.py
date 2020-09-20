from math import sqrt


class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(1, round(sqrt(i)) + 2):
                if i % j == 0 and dp[i - j] is False:
                    dp[i] = True
                    break
        return dp[N]
