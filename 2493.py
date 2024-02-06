import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

result = [0] * N
stack = []

for i in range(N):
    while stack:
        if towers[stack[-1][0]] < towers[i]:
            stack.pop()
        else:
            result[i] = stack[-1][0] + 1
            break
    stack.append((i, towers[i]))
print(*result)
