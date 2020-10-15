from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            # Keeps track of two most recent maximum values
            dp = [0, nums[0] if len(nums) > 0 else 0]
            for i, num in enumerate(nums[1:]):
                # Either choose the maximum sum of one house before
                # or maximum sum of two houses before plus the current one
                if dp[0] + num > dp[1]:
                    dp[0], dp[1] = dp[1], dp[0] + num
                else:
                    dp[0] = dp[1]
            return dp[1]

        if len(nums) == 1:
            return nums[0]

        # To accomodate for circularity of the houses,
        # Choose from the greater of the sum from second house to last and the sum
        # from the first house to the second last
        return max(helper(nums[1:]), helper(nums[:-1]))
