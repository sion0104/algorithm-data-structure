from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for _ in range(N):
    line = list(map(str, sys.stdin.readline().split()))

    if line[0] == 'push':
        queue.append(int(line[1]))
    elif line[0] == 'pop':
        print(queue.pop() if queue else -1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        print(0 if queue else 1)
    else:
        print(queue[-1] if queue else -1)


