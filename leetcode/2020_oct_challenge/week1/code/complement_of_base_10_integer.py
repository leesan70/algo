class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join(list(map(lambda d: '0' if d == '1' else '1', bin(N)[2:]))), 2)
