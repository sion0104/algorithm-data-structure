import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

vertices = [[] for _ in range(N+1)]
parent = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

queue = deque()
queue.append(1)

while queue:
    current = queue.popleft()
    for vertex in vertices[current]:
        if parent[vertex] == 0:
            parent[vertex] = current
            queue.append(vertex)

print('\n'.join(map(str, parent[2:])))
