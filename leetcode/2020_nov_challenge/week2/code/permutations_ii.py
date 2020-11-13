class Solution:
    def permuteUnique(self, nums):
        def dfs(ind, built):
            if ind == len(nums):
                ans.append(built)
                return

            stop = built.index(nums[ind]) if nums[ind] in built else ind

            for i in range(stop + 1):
                dfs(ind + 1, built[:i] + [nums[ind]] + built[i:])

        ans = []
        dfs(0, [])
        return ans
