"""
랜덤한 정수 배열이 주어지면 중복된 원소의 값을 모두 프린트 하시오. 단, 공간복잡도 O(1)이여야 합니다.

Given an integer array, print all non unique elements.


input: [0, 6, 3, 4, 0]

output: 0


input: [5, 4, 3, 2, 1, 1, 1, 1, 1, 2]

output: 1, 2
"""


def print_repetition(input_array):
    prev = None
    rep = False

    for elem in sorted(input_array):
        if elem == prev:
            if not rep:
                print(elem)
                rep = True
        else:
            rep = False
        prev = elem

print_repetition([5, 4, 3, 2, 1, 1, 1, 1, 1, 2])