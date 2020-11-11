from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            i, j = 0, len(row) - 1
            while i <= j:
                if row[i] == row[j]:
                    # pixel ^ 1 will invert the bit
                    row[i], row[j] = row[i] ^ 1, row[j] ^ 1
                i += 1
                j -= 1
        return A
