# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        node_copy = Node(node.val)
        clone_dict = { node: node_copy }
        stack = [node]
        while stack:
            curr_node = stack.pop()
            for neighbor in curr_node.neighbors:
                if neighbor not in clone_dict:
                    stack.append(neighbor)
                    clone_dict[neighbor] = Node(neighbor.val)
                clone_dict[curr_node].neighbors.append(clone_dict[neighbor])
        return node_copy
