import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

visit = [False for _ in range(v+1)]
heap = [[0, 1]]
total_cost = 0
count = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

while heap:
    if count == v:
        break

    cost, vertex = heapq.heappop(heap)
    if not visit[vertex]:
        visit[vertex] = True
        total_cost += cost
        count += 1
        for edge in graph[vertex]:
            next_cost, next_vertex = edge
            if not visit[next_vertex]:
                heapq.heappush(heap, [next_cost, next_vertex])

print(total_cost)
