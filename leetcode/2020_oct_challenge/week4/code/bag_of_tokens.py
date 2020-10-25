from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        sorted_ = sorted(tokens)
        up_i = 0
        down_i = len(sorted_) - 1
        while up_i <= down_i:
            if P < sorted_[up_i]:
                if score > 0  and down_i - up_i > 1:
                    P += sorted_[down_i]
                    score -= 1
                    down_i -= 1
                else:
                    break
            else:
                P -= sorted_[up_i]
                score += 1
                up_i += 1
        return score
