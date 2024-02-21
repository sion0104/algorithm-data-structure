import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = 999999
houses, chickens = [], []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            houses.append([i, j])
        elif graph[i][j] == 2:
            chickens.append([i, j])

for chicken in combinations(chickens, M):
    temp = 0
    for house in houses:
        chicken_len = 999
        for j in range(M):
            chicken_len = min(chicken_len, abs(house[0]-chicken[j][0])+abs(house[1]-chicken[j][1]))
        temp += chicken_len
    result = min(result, temp)

print(result)
