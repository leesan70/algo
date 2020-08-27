import unittest

"""
Return minimum number of coins to be removed in a pile of coins A to satisfy
the following requirements.

1) If i <= j, |A[i] - A[j]| <= K, for a given non-negative number K
2) You can only remove coins, not add them to another spot

Ex:

Input: A = [2, 2, 2, 2], K = 0
Output: 0

Input: A = [1, 2, 5, 1, 1, 1], K = 3
Output: 1 (By removing 1 coin from 5)

Input: A = [1, 5, 1, 2, 5, 1], K = 3
Output: 2

Input: A = [1, 2, 6, 10], K = 3
Output: 4 (By removing 1, 2 completely and removing 1 from 10)

Input: A = [2, 2, 10, 12, 16], K = 2
Output: 6 (By removing 2, 2 completely and 2 from 16

Input: A = [2, 2, 8, 2, 5], K = 3
Output: 3 (By removing 3 coins from 8)

"""

def coin_piles_wrong_assumption(A, K):
    # Code based on the assumption that i + 1 == j (only immediate neighbors)
    removed = 0
    temp = None
    for i in range(1, len(A)):
        prev = temp if temp else A[i-1]
        diff = prev - A[i]
        abs_diff = abs(diff)
        if abs_diff > K:
            removed += abs_diff - K
            if prev <= A[i]:
                temp = A[i] - abs_diff + K
                continue
        temp = None
    return removed


def coin_piles(A, K):
    removed = 0
    temp = None
    for i in range(1, len(A)):
        prev = temp if temp else A[i-1]
        diff = prev - A[i]
        abs_diff = abs(diff)
        if abs_diff > K:
            removed += abs_diff - K
            if prev <= A[i]:
                temp = A[i] - abs_diff + K
                continue
        temp = None
    return removed


class Test(unittest.TestCase):

    def test_no_removal(self):
        A = [2, 2, 2, 2]
        K = 0
        self.assertEqual(coin_piles(A, K), 0)

    def test_ex1(self):
        A = [1, 2, 5, 1, 1]
        K = 3
        self.assertEqual(coin_piles(A, K), 1)

    def test_ex2(self):
        A = [1, 5, 1, 2, 5, 1]
        K = 3
        self.assertEqual(coin_piles(A, K), 2)

    def test_more_than_one_index_diff(self):
        A = [1, 2, 6, 10]
        K = 3
        self.assertEqual(coin_piles(A, K), 3)


if __name__ == "__main__":
    unittest.main()
