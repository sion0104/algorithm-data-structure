import sys
from collections import deque

v = int(sys.stdin.readline())
e = int(sys.stdin.readline())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [False for _ in range(v + 1)]


def BFS(a):
    queue = deque([a])
    count = 0
    visited[a] = True
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                count += 1

    return count


print(BFS(1))
