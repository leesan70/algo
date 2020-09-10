# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderTraversal(root: TreeNode):
    elemList = []
    if root is None:
        return elemList
    if root.left:
        elemList = inOrderTraversal(root.left)
    elemList.append(root.val)
    if root.right:
        rightList = inOrderTraversal(root.right)
        elemList.extend(rightList)
    return elemList


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        root1ElemList = inOrderTraversal(root1)
        root2ElemList = inOrderTraversal(root2)
        allElemList = []
        i, j = 0, 0
        while i < len(root1ElemList) or j < len(root2ElemList):
            elem1 = root1ElemList[i] if i < len(root1ElemList) else None
            elem2 = root2ElemList[j] if j < len(root2ElemList) else None
            if elem1 is None:
                allElemList.append(elem2)
                j += 1
            elif elem2 is None:
                allElemList.append(elem1)
                i += 1
            else:
                if elem1 < elem2:
                    allElemList.append(elem1)
                    i += 1
                else:
                    allElemList.append(elem2)
                    j += 1
        return allElemList
