class Solution:
    def maxPower(self, s: str) -> int:
        max_count = 0
        curr_count = 0
        prev_ch = s[0]
        for ch in s:
            if prev_ch == ch:
                curr_count += 1
            else:
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
            prev_ch = ch
        return max_count
