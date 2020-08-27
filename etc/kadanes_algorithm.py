"""
Given an array containing both negative and positive integers. Find the
contiguous sub-array with maximum sum.

Ex)

Input: [1, 2, 3]
Output: 6

Input: [-1, -2, -3, -4]
Output: -1
"""

def kadane(input_array):
    dp = [[elem] for elem in input_array]
