import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, N + 1)])
result = []

for _ in range(N):
    index = (K - 1) % len(queue)

    element = queue[index]
    queue.remove(element)
    result.append(element)

    queue.rotate(-index)

print("<" + ", ".join(map(str, result)) + ">")
