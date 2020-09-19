from typing import List


class Solution:
    def generateSeq(self, num: int) -> int:
        mod = num % 10
        if mod != 0 and mod != 9:
            return num * 10 + mod + 1
        return False

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        all_seq = []
        for dig in range(1, 9):
            seq = dig
            while True:
                seq = self.generateSeq(seq)
                if seq is False or seq > high:
                    break
                if seq >= low:
                    all_seq.append(seq)
        return sorted(all_seq)
