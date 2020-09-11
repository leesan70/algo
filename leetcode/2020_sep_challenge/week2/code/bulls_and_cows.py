class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_list, cow_list = [0 for _ in range(10)], []
        secret_count, guess_count = [0 for _ in range(10)], [0 for _ in range(10)]
        for i, (d1, d2) in enumerate(zip(secret, guess)):
            if d1 == d2:
                bull_list[int(d1)] += 1
            secret_count[int(d1)] += 1
            guess_count[int(d2)] += 1
        for i, (c1, c2) in enumerate(zip(secret_count, guess_count)):
            cow_list.append(min(c1, c2) - bull_list[i])
        return "{}A{}B".format(sum(bull_list), sum(cow_list))


# better implementation
# class Solution:
#     def getHint(self, secret: str, guess: str) -> str:
#         bulls, cows = 0, 0
#         counter = collections.defaultdict(int)
#
#         for idx in range(len(secret)):
#             s = secret[idx]
#             g = guess[idx]
#
#             if s == g:
#                 bulls += 1
#             else:
#                 if counter[s] < 0:
#                     cows += 1
#                 if counter[g] > 0:
#                     cows += 1
#                 counter[s] += 1
#                 counter[g] -= 1
#         return f"{bulls}A{cows}B"
