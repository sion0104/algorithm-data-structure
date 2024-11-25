import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

cols, rows, heights = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(rows)] for _ in range(heights)]
visited = [[[False] * cols for _ in range(rows)] for _ in range(heights)]

queue = deque()

for height in range(heights):
    for row in range(rows):
        for col in range(cols):
            if tomatoes[height][row][col] == 1:
                queue.append((height, row, col))

while queue:
    height, row, col = queue.popleft()

    for i in range(6):
        nx = dx[i] + col
        ny = dy[i] + row
        nz = dz[i] + height

        if 0 > nx or nx >= cols or 0 > ny or ny >= rows or 0 > nz or nz >= heights:
            continue

        if tomatoes[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
            visited[nz][ny][nx] = True
            tomatoes[nz][ny][nx] = tomatoes[height][row][col] + 1
            queue.append((nz, ny, nx))

day = 0
for height in tomatoes:
    for row in height:
        for col in row:
            if col == 0:
                print(-1)
                exit(0)
        day = max(day, max(row))

print(day - 1)
