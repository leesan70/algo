from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def dfs(st, end):
            if end - st <= 1:
                return target in nums[st: end + 1]

            mid = (st + end) // 2
            if nums[mid] > nums[end]:  # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(st, mid)
                else:
                    return dfs(mid + 1, end)
            elif nums[mid] < nums[end]:  # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end)
                else:
                    return dfs(st, mid)
            # duplicates from mid to end. have to look in all of the current search space
            else:
                return dfs(mid + 1, end) or dfs(st, mid)

        return dfs(0, len(nums) - 1)
