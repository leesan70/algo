from typing import List


class Solution:
    def isNonDecreasing(self, nums):
        len_nums = len(nums)
        if len_nums <= 1:
            return (True, None)
        for i in range(len_nums - 1):
            if nums[i] > nums[i+1]:
                return (False, i)
        return (True, None)

    def checkPossibility(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        isAlreadyNonDecreasing, index = self.isNonDecreasing(nums)
        if isAlreadyNonDecreasing:
            return True
        # Should change first element.
        if index == 0:
            return self.isNonDecreasing(nums[1:])[0]
        # Element that has prev and next elements. Should see if change is compatible.
        elif 0 < index < len_nums - 2:
            if nums[index+1] - nums[index-1] >= 1:
                return self.isNonDecreasing(nums[index+1:])[0]
            elif index+2 < len_nums and nums[index+2] - nums[index] >= 1:
                return self.isNonDecreasing(nums[index+2:])[0]
        # Should change last element. It can go up to 10000 as per constraint.
        elif nums[len_nums - 1] < 10000:
            return True


if __name__ == "__main__":
    test_cases = [
        # [1, 3, 2],
        # [1, 2, 5, 3, 3]
        [2, 3, 3, 2, 4]
    ]
    s = Solution()
    for test_case in test_cases:
        print(s.checkPossibility(test_case))
