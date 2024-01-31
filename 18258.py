import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())

for _ in range(N):
    line = sys.stdin.readline().split()

    if line[0] == 'push':
        queue.append(int(line[1]))
    elif line[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        print(0 if queue else 1)
    elif line[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[-1] if queue else -1)

