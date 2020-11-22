from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        len_n = len(n_str)
        # dp[i] = total number of valid integers for N[i:]
        dp = [0] * len_n + [1]
        for i in range(len_n - 1, -1, -1):
            for digit in digits:
                if digit < n_str[i]:
                    dp[i] += len(digits) ** (len_n - i - 1)
                elif digit == n_str[i]:
                    dp[i] += dp[i + 1]
        prev_sum = sum(len(digits) ** i for i in range(1, len_n))
        return dp[0] + prev_sum
