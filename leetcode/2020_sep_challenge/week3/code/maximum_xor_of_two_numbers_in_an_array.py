from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        # Build the answer from the highest bit, one bit at a time
        for i in reversed(range(32)):
            prefixes = set([num >> i for num in nums]) # right shift for comparison
            ans <<= 1 # left shift to process next bit
            candidate = ans + 1 # we could have either 0 or 1 at this lowest bit
            if any(candidate ^ p in prefixes for p in prefixes):
                # if candidate ^ p matches q in prefixes, then p ^ q matches candidate
                ans = candidate
        return ans
