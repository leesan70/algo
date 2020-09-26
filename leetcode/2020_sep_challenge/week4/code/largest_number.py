from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        candidate = "".join(sorted(map(str, nums), key=cmp_to_key(
            lambda a, b: int(b + a) - int(a + b)
        )))
        return candidate if candidate[0] != "0" else "0"
