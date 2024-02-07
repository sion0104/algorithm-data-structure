from sys import stdin
from collections import deque

input = stdin.readline

N, M, R = map(int, input().split())

matrix = []
result = [[0]*M for _ in range(N)]
queue = deque()

for i in range(N):
    matrix.append(list(input().split()))

loops = min(N, M) // 2

for i in range(loops):
    queue.clear()
    queue.extend(matrix[i][i:M-i])
    queue.extend([row[M-1-i] for row in matrix[i+1:N-1-i]])
    queue.extend(matrix[N-1-i][i:M-i][::-1])
    queue.extend([row[i] for row in matrix[i+1:N-1-i][::-1]])

    queue.rotate(-R)

    for j in range(i, M-i):
        result[i][j] = queue.popleft()
    for j in range(i+1, N-1-i):
        result[j][M-1-i] = queue.popleft()
    for j in range(M-1-i, i-1, -1):
        result[N-1-i][j] = queue.popleft()
    for j in range(N-2-i, i, -1):
        result[j][i] = queue.popleft()

for row in result:
    print(" ".join(row))
