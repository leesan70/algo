"""
Given a sorted array of integers, every element appears twice except for one.
Find that single one in linear time complexity and without using extra memory.

Example:

Input:

1
11
1 1 2 2 3 3 4 50 50 65 65

Output:

4
"""


def once_in_array(input_array):
    count = 0
    current = None
    for i in range(len(input_array)):
        elem = input_array[i]
        if not current:
            current = elem
            count = 1
            continue
        if count == 1:
            if elem == current:
                count = 2
                continue
            return input_array[i - 1]
        count = 1
        current = elem
    return input_array[-1]


def str_to_array(input_str):
    return list(filter(None, input_str.replace('\n', "").split(" ")))


def main():
    import sys
    lines = sys.stdin.readlines()
    for i in range(int(lines[0])):
        input_str = lines[i*2 + 2]
        print(once_in_array([int(elem) for elem in str_to_array(input_str)]))


if __name__ == "__main__":
    main()