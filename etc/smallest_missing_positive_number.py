"""
Ex)
Input: [-10, 5, 2, 0, -20, 1, 10]
Output: 3

Input: [1, 5, 2, -10, 0, 4, 3]
Output: 6

Time Complexity: O(N)
Space Complexity: O(1)

Non-positive number = trap
First pass -> count number of non-positives
           -> upper bound on the array = len(array) + 1 - count_non_pos

Second pass ->if anything bigger than this upper bound, upper bound - 1
"""


def smpn(input_array):
    upper_bound = len(input_array) + 1
    for elem in input_array:
        if elem <= 0:
            upper_bound -= 1
    for elem in input_array:
        if elem >= upper_bound:
            upper_bound -= 1
    return upper_bound


if __name__ == "__main__":
    input1 = [-10, 5, 2, 0, -20, 1, 10]
    print(smpn(input1))

    input2 = [1, 5, 2, -10, 0, 4, 3]
    print(smpn(input2))
