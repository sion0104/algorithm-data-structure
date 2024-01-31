import sys

K, N = map(int, sys.stdin.readline().split())
lengths = []

for _ in range(K):
    lengths.append(int(sys.stdin.readline()))

start, end = 1, max(lengths)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(K):
        count += lengths[i] // mid

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)