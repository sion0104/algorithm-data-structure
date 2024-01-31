from collections import deque
import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    start, destination = map(int, sys.stdin.readline().split())
    graph[start][destination] = graph[destination][start] = 1

visited1 = [0] * (N + 1)
visited2 = visited1.copy()


def DFS(V):
    visited1[V] = 1
    print(V, end=' ')
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited1[i] == 0:
            DFS(i)


def BFS(V):
    queue = [V]
    visited2[V] = 1
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if visited2[i] == 0 and graph[V][i] == 1:
                queue.append(i)
                visited2[i] = 1

DFS(V)
print()
BFS(V)
