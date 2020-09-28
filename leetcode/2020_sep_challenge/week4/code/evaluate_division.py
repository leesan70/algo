from typing import List


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class Solution:
    def buildGraph(self, equations, values):
        dict_ = {}
        for i, eq in enumerate(equations):
            src, dest = eq[0], eq[1]
            if src not in dict_:
                dict_[src] = []
            if dest not in dict_:
                dict_[dest] = []
            dict_[src].append(Node(dest, values[i]))
            dict_[dest].append(Node(src, 1 / values[i]))
        return dict_

    def dfs(self, src, dest, visited, graph):
        if not src in graph or not dest in graph:
            return -1.
        if src == dest:
            return 1.
        visited.add(src)
        for node in graph[src]:
            if node.key not in visited:
                val = self.dfs(node.key, dest, visited, graph)
                if val != -1.:
                    return node.val * val
        return -1.

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = self.buildGraph(equations, values)
        for i, q in enumerate(queries):
            result.append(self.dfs(q[0], q[1], set(), graph))
        return result
