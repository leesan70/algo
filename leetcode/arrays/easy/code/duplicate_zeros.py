# from collections import deque
from typing import List


class Solution:
    # using O(n) space, O(n) time
    # def duplicateZeros(self, arr: List[int]) -> None:
    #     """
    #     Do not return anything, modify arr in-place instead.
    #     """
    #     if len(arr) == 0:
    #         return
    #     saved = deque()
    #     for i in range(len(arr)):
    #         if arr[i] == 0:
    #             saved.append(0)
    #             saved.append(0)
    #         else:
    #             saved.append(arr[i])
    #         arr[i] = saved.popleft()
    #     return

    # using O(1) space with array 2 pass O(n) time
    # count where the cut off is in the first pass
    # fill from the back in the second pass
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if len(arr) == 0:
            return
        last_index = 0
        dest_index = 0
        zero_went_over = False
        for i, num in enumerate(arr):
            if num == 0:
                dest_index += 2
            else:
                dest_index += 1
            if dest_index == len(arr):
                last_index = i
                break
            elif dest_index > len(arr):
                last_index = i
                zero_went_over = True
                break

        curr_index = len(arr) - 1
        for i in range(last_index, -1, -1):
            if arr[i] == 0:
                if i == last_index and zero_went_over:
                    arr[curr_index] = 0
                    curr_index -= 1
                else:
                    arr[curr_index], arr[curr_index - 1] = 0, 0
                    curr_index -= 2
            else:
                arr[curr_index] = arr[i]
                curr_index -= 1
        return
