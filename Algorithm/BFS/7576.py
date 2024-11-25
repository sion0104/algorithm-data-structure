import sys
from collections import deque

input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cols, rows = map(int, input().strip().split())

tomatoes = []

for _ in range(rows):
    tomatoes.append(list(map(int, input().strip().split())))

Q = deque()

for row in range(rows):
    for col in range(cols):
        if tomatoes[row][col] == 1:
            Q.append((row, col))

while Q:
    length = len(Q)
    for _ in range(length):
        row, col = Q.popleft()

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if rows > nr >= 0 and 0 <= nc < cols and tomatoes[nr][nc] == 0:
                tomatoes[nr][nc] = tomatoes[row][col] + 1
                Q.append((nr, nc))

day = 0
for row in tomatoes:
    for tomato in row:
        if tomato == 0:
            print(-1)
            exit(0)
    day = max(day, max(row))

print(day - 1)
