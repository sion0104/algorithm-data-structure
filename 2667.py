import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]


def BFS(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count_node = 1
    queue = deque([(x, y)])
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for w in range(4):
            nx, ny = x + dx[w], y + dy[w]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count_node += 1
            else:
                continue
    return count_node


result = [BFS(graph, i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

result.sort()
print(len(result))

for i in range(len(result)):
    print(result[i])
