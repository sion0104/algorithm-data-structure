from collections import deque
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

result = deque()

for i in range(N):
    if A[i] == 0:
        result.appendleft(B[i])

for j in range(M):
    result.append(C[j])
    print(result.popleft(), end=' ')

