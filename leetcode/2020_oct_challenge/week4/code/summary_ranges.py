from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []
        if len(nums) == 0:
            return results
        st, end = 0, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[end] + 1:
                end += 1
            else:
                if st == end:
                    results.append(str(nums[st]))
                else:
                    results.append("{}->{}".format(nums[st], nums[end]))
                st, end = i, i
        if st == end:
            results.append(str(nums[st]))
        else:
            results.append("{}->{}".format(nums[st], nums[end]))
        return results
