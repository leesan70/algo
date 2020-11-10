# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def getMinMax(node, minmax):
            l_mm = (min(node.val, minmax[0]), max(node.val, minmax[1]))
            r_mm = l_mm
            if node.left is not None:
                l_mm = getMinMax(node.left, l_mm)
            if node.right is not None:
                r_mm = getMinMax(node.right, r_mm)
            return l_mm if l_mm[1] - l_mm[0] >= r_mm[1] - r_mm[0] else r_mm

        minmax = getMinMax(root, (1e10, -1e10))
        return minmax[1] - minmax[0]
