class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i = 0, num_repeat = 1):
            result = ""
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    sub_repeat = int(ch)
                    while s[i+1].isdigit():
                        i += 1
                        sub_repeat = 10 * sub_repeat + int(s[i])
                    sub_str, i = helper(i + 2, sub_repeat)
                    result += sub_str
                elif ch == ']':
                    result *= num_repeat
                    return result, i
                else:
                    result += ch
                i += 1
            return result, i
        return helper()[0]
