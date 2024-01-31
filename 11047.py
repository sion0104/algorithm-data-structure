import sys

N, K = map(int, sys.stdin.readline().split())
count = 0
nums = []

for _ in range(N):
    num = nums.append(int(sys.stdin.readline()))

nums.sort(reverse=True)

for num in nums:
    if num <= K:
        count += K // num
        K = K % num
        if K <= 0:
            break

print(count)
