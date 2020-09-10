from collections import deque


def get_neighbors(r, c):
    global n, m
    neighbors = []
    dx = [0, -1, 1, 0]
    dy = [-1, 0, 0, 1]
    for i in range(4):
        new_r = r + dy[i]
        new_c = c + dx[i]
        if 0 <= new_r < n and 0 <= new_c < m:
            neighbors.append((new_r, new_c))
    return neighbors


def bfs(r, c):
    global container, visited, count
    if container[r][c] == "1" or visited[r][c]:
        return
    count += 1
    queue = deque([(r, c)])
    while queue:
        cell_r, cell_c = queue.popleft()
        if container[cell_r][cell_c] == "1" or visited[cell_r][cell_c]:
            continue
        visited[cell_r][cell_c] = True
        neighbors = get_neighbors(cell_r, cell_c)
        for neighbor in neighbors:
            queue.append(neighbor)


n, m = map(int, input().split(" "))
count = 0
container = []
for _ in range(n):
    row = input()
    if len(row) != m:
        raise Exception("invalid dimensions")
    container.append(row)

visited = [[False for _ in range(m)] for _ in range(n)]
print("n: {}, m: {}".format(n, m))
print("Graph")
for row in container:
    print(row)

for i in range(n):
    for j in range(m):
        bfs(i, j)

print("Count: {}".format(count))

# EX1:
# 4 5
# 00110
# 00011
# 11111
# 00000
#
# Count: 3

# EX2:
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
#
# Count: 8
