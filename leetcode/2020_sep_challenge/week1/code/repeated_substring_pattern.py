class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        curr_interval = 1
        while curr_interval < len(s) // 2 + 1:
            if len(s) % curr_interval == 0:
                pattern_matched = True
                for i in range(len(s) // curr_interval - 1):
                    if s[i * curr_interval: (i + 1) * curr_interval] != s[(i+1) * curr_interval : (i+2) * curr_interval]:
                        pattern_matched = False
                if pattern_matched:
                    return True
            curr_interval += 1
        return False