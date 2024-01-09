import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(x, y):
    queue = deque([(x, y)])
    cabbages[x][y] = 0

    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and cabbages[nx][ny] == 1:
                queue.append((nx, ny))
                cabbages[nx][ny] = 0
            else:
                continue


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbages = [[0] * N for _ in range(M)]
    count = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        cabbages[X][Y] = 1

    for x in range(M):
        for y in range(N):
            if cabbages[x][y] == 1:
                BFS(x, y)
                count += 1

    print(count)
