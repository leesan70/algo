n, m = map(int, input().split())
char_x, char_y, char_dir = map(int, input().split())
visited = [[0] * m for _ in range(n)]
visited[char_x][char_y] = 1
game_map = []
count, turn_count = 1, 0
for _ in range(n):
    game_map.append(list(map(int, input().split())))

# N, E, S, W
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def turn_left():
    global char_dir, turn_count
    char_dir = char_dir - 1 if char_dir - 1 > 0 else 3
    turn_count += 1


while True:
    while turn_count < 4:
        print(char_x, char_y, char_dir, visited)
        turn_left()
        nx, ny = char_x + dx[char_dir], char_y + dy[char_dir]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if game_map[nx][ny] == 0 and visited[nx][ny] == 0:
            count += 1
            visited[nx][ny] = 1
            char_x, char_y = nx, ny
            break
    if turn_count == 4:
        nx, ny = char_x - dx[char_dir], char_y - dy[char_dir]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or game_map[nx][ny] == 1:
            break
        if visited[nx][ny] == 0:
            count += 1
            visited[nx][ny] = 1
        char_x, char_y = nx, ny
    turn_count = 0

print(count)
