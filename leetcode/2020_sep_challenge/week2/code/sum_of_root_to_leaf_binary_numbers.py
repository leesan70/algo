# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def helper(root: TreeNode, cum_sum: int) -> int:
            my_sum = cum_sum * 2 + root.val
            left_sum = helper(root.left, my_sum) if root.left else 0
            right_sum = helper(root.right, my_sum) if root.right else 0
            return left_sum + right_sum + (0 if root.left or root.right else my_sum)
        return helper(root, 0)