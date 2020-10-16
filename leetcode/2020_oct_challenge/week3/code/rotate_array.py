from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, start, end):
            for i in range((end - start + 1) // 2):
                nums[start + i], nums[end - i - 1] = nums[end - i - 1], nums[start + i]

        k = k % len(nums)

        reverse(nums, 0, len(nums) - k)
        reverse(nums, len(nums) - k, len(nums))
        reverse(nums, 0, len(nums))
