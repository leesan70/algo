class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = list(filter(lambda w: w != '', s.split(" ")))
        return len(split[-1]) if len(split) > 0 else 0
