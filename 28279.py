from collections import deque
import sys

N = int(sys.stdin.readline())
result = deque()

for _ in range(N):
    line = sys.stdin.readline().rstrip()

    if line[0] == '1':
        result.appendleft(int(line[2:]))
    elif line[0] == '2':
        result.append(int(line[2:]))
    elif line[0] == '3':
        print(result.popleft() if result else -1)
    elif line[0] == '4':
        print(result.pop() if result else -1)
    elif line[0] == '5':
        print(len(result))
    elif line[0] == '6':
        print(0 if result else 1)
    elif line[0] == '7':
        print(result[0] if result else -1)
    elif line[0] == '8':
        print(result[-1] if result else -1)