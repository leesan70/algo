class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        curr_result = []
        for i, ch in enumerate(s):
            if ch not in curr_result:
                # If current char is smaller than then last character in our result, and
                # that last character appears later in our input string, we can use the char that appears later on
                while curr_result and ch < curr_result[-1] and i < last_index[curr_result[-1]]:
                    curr_result.pop()
                curr_result.append(ch)
        return ''.join(curr_result)
