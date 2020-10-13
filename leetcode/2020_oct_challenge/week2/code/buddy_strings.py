class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # idea)
        # strings should either match with a count of a character of two or more,
        # or should differ exactly in two positions, with the characters eligible for a valid swap
        if len(A) != len(B):
            return False
        diff_indices = []
        counterA = dict()

        for i in range(len(A)):
            if A[i] != B[i]:
                diff_indices.append(i)
            if A[i] not in counterA:
                counterA[A[i]] = 1
            else:
                counterA[A[i]] += 1

        if len(diff_indices) == 0:
            if any(map(lambda c: c[1] > 1, counterA.items())):
                return True
            return False
        elif len(diff_indices) != 2:
            return False

        if A[diff_indices[1]] == B[diff_indices[0]] and A[diff_indices[0]] == B[diff_indices[1]]:
            return True
        return False
