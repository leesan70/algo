from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.num_path = 0
        self.num_empty = sum(map(lambda row: len(list(filter(lambda c: c == 0, row))), grid))
        num_visited = -1

        start_location = None
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    start_location = (r, c)
                    break
            if start_location:
                break
        visited = [[False for _ in r] for r in grid]
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]

        def dfs_backtracking(r, c, num_visited):
            if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or \
                    grid[r][c] == -1 or visited[r][c]:
                return
            if grid[r][c] == 2 and num_visited == self.num_empty:
                self.num_path += 1
            else:
                saved = visited[r][c]
                visited[r][c] = True
                for i in range(4):
                    dfs_backtracking(r + dx[i], c + dy[i], num_visited + 1)
                visited[r][c] = saved

        dfs_backtracking(*start_location, num_visited)

        return self.num_path
