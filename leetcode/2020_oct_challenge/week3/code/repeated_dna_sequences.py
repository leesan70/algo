# Could not solve
# Reference https://leetcode.com/problems/repeated-dna-sequences/discuss/898299/Python-2-lines-solution-explained
import collections
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = collections.Counter(s[i:i+10] for i in range(0, len(s) - 9))
        return [key for key in counter if counter[key] > 1]
