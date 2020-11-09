# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def tilt(r: TreeNode) -> int:
            sum_val_left, sum_val_right = 0, 0
            sum_tilt_left, sum_tilt_right = 0, 0
            if r.left is not None:
                sum_val_left, sum_tilt_left = tilt(r.left)
            if r.right is not None:
                sum_val_right, sum_tilt_right = tilt(r.right)
            curr_tilt = abs(sum_val_left - sum_val_right)
            # print(r.val, sum_val_left, sum_val_right, sum_tilt_left, sum_tilt_right, curr_tilt)
            return (r.val + sum_val_left + sum_val_right, curr_tilt + sum_tilt_left + sum_tilt_right)

        return tilt(root)[1]
