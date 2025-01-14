from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10 ** 5

visited = [0] * (MAX + 1)


def bfs(a, b):
    queue = deque([a])
    visited[a] = 0

    while queue:
        x = queue.popleft()
        if x == b:
            return

        for nx in (2 * x, x - 1, x + 1):
            if nx < 0 or nx > MAX or visited[nx]:
                continue
            if nx == 2 * x:
                visited[nx] = visited[x]
            else:
                visited[nx] = visited[x] + 1
            queue.append(nx)


bfs(N, K)
print(visited[K])
