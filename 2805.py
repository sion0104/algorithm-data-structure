import sys

input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

start, end = 0, max(heights)

while start <= end:
    sum, mid = 0, (start + end) // 2

    for height in heights:
        if height > mid:
            sum += height - mid

    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)