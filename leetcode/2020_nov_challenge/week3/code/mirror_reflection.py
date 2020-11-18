class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = 1
        while k * q % p:
            k += 1
        if k % 2 == 1 and (k * q // p) % 2 == 0:
            return 0
        if k % 2 == 1 and (k * q // p) % 2 == 1:
            return 1
        if k % 2 == 0 and (k * q // p) % 2 == 1:
            return 2
