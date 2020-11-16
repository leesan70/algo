# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        range_sum = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if low <= node.val <= high:
                range_sum += node.val
            if node.left and low <= node.val:
                stack.append(node.left)
            if node.right and node.val <= high:
                stack.append(node.right)
        return range_sum
