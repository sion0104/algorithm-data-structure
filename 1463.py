import sys

N = int(sys.stdin.readline())
queue = [0] * (N+1)

for i in range(2, N + 1):
    queue[i] = queue[i-1] + 1

    if i % 3 == 0 and i % 2 == 0:
        queue[i] = min(queue[i//3]+1, queue[i//2]+1, queue[i])
    elif i % 3 == 0:
        queue[i] = min(queue[i//3]+1, queue[i])
    elif i % 2 == 0:
        queue[i] = min(queue[i//2]+1, queue[i])

print(queue[N])
