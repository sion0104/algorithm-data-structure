from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
result = []

while queue:
    index, num = queue.popleft()
    result.append(index)

    if num > 0:
        queue.rotate(-(num-1))
    else :
        queue.rotate(-num)

print(' '.join(map(str, result)))
