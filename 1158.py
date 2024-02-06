import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([i for i in range(1, N+1)])
result = []


while queue:
    queue.rotate(-(K-1))
    num = queue.popleft()
    result.append(str(num))

print("<", end="")
print(', '.join(result), end="")
print(">", end="")

