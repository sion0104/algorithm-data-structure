import sys

N, K = map(int, sys.stdin.readline().split())
array = []

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    array.append((A, B))

array.sort(key=lambda x: (-(x[0]-x[1])))

count, plus = 0, 0
for n in array:

    if n[0] >= n[1]+plus:
        count += 1
    else:
        plus = n[1] - n[0]
        count += 1

    if count == K:
        break

print(plus)
