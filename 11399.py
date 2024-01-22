import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

result = 0
for i in range(N+1):
    result += sum(P[0:i])
print(result)