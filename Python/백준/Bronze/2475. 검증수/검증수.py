import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

result = 0
for num in nums:
    result += num ** 2

print(result % 10)
