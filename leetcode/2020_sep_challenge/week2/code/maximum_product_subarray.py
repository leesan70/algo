from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        local_max = nums[0]
        local_min = nums[0]
        for num in nums[1:]:
            temp_local_max = local_max
            local_max = max(local_max * num, local_min * num, num)
            local_min = min(temp_local_max * num, local_min * num, num)
            if local_max > global_max:
                global_max = local_max
        return global_max