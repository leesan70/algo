# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS Solution with O(2 ^ h) space
        #         if root is None:
        #             return None
        #         curr_stack = [root]
        #         next_stack = []

        #         prev_node = None
        #         while curr_stack:
        #             # pop left the current stack as curr_node
        #             # also queue up the children nodes to next_stack, if present
        #             curr_node = curr_stack.pop(0)
        #             if curr_node.left is not None:
        #                 next_stack.append(curr_node.left)
        #                 next_stack.append(curr_node.right)
        #             # if prev_node exists, set curr_node as next
        #             if prev_node:
        #                 prev_node.next = curr_node

        #             # at the last node of a depth. reset prev_node and switch curr_stack to next_stack
        #             if len(curr_stack) == 0:
        #                 curr_node.next = None
        #                 prev_node = None
        #                 curr_stack = next_stack
        #                 next_stack = []
        #             # still has nodes left in this depth. set prev_node to curr_node
        #             else:
        #                 prev_node = curr_node

        #         return root

        # Tree level order traversal with O(1) Space solution
        if not root:
            return None
        # Store next_level as left child of the first node at a level
        curr = root
        next_level = root.left

        while next_level:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
                curr = curr.next
            else:
                curr = next_level
                next_level = curr.left
        return root
