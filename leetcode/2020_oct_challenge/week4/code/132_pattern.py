# Couldn't solve
# https://leetcode.com/problems/132-pattern/discuss/906876/Python-O(n)-solution-with-decreasing-stack-explained
from itertools import accumulate
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)

        for j in range(n - 1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
