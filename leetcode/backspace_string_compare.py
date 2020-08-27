import itertools

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         def build(s):
#             ans = []
#             for ch in s:
#                 if ch != '#':
#                     ans.append(ch)
#                 else:
#                     if len(ans) > 0:
#                         ans.pop()
#             return "".join(ans)
#         return build(S) == build(T)

class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

s_list = ['ab#c', 'ab##', 'a##c', 'a#c', "nzp#o#g", 'xywrrmp']
t_list = ['ad#c', 'c#d#', '#a#c', 'b', "b#nzp#o#g", 'xywrrm#p']
# s_list = ['xywrrmp']
# t_list = ['xywrrm#p']

sol = Solution()
for s, t in zip(s_list, t_list):
    print(sol.backspaceCompare(s, t))
