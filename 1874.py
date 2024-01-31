import sys
from collections import deque

n = int(sys.stdin.readline())

count = 1
condition = True
stack, result = deque(), deque()

for _ in range(n):
    num = int(sys.stdin.readline())

    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        condition = False
        break

print('\n'.join(result)) if condition else print('NO')
