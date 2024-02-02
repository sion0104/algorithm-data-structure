import sys

N, M = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0]+ array

for i in range(1, N):
    prefix_sum[i+1] += prefix_sum[i]

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end]-prefix_sum[start-1])
