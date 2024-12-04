import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])

start, end = map(int, input().split())
costs = [1e9 for _ in range(N+1)]

heap = []
costs[start] = 0

heapq.heappush(heap, [start, 0])

while heap:
    current_city, current_cost = heapq.heappop(heap)
    if costs[current_city] < current_cost:
        continue

    for next_city, next_cost in graph[current_city]:
        sum_cost = current_cost + next_cost
        if sum_cost >= costs[next_city]:
            continue

        costs[next_city] = sum_cost
        heapq.heappush(heap, [next_city, sum_cost])

print(costs[end])
