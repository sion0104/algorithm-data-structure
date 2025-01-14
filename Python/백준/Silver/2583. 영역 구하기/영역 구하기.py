import sys
from collections import deque

input = sys.stdin.readline

Y, X, K = map(int, input().split())
graph = [[0] * X for _ in range(Y)]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < Y and 0 <= nx < X and graph[ny][nx] == 0:
                graph[ny][nx] += 1
                q.append((ny, nx))
                cnt += 1

    return cnt

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            graph[y][x] += 1

result = []

for y in range(Y):
    for x in range(X):
        if graph[y][x] == 0:
            graph[y][x] += 1
            result.append(bfs(y, x))

print(len(result))
print(*sorted(result))
