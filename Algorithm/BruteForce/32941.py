import sys

input = sys.stdin.readline

T, X = map(int, input().strip().split())
N = int(input().strip())

result = True

for _ in range(N):
    K = int(input().strip())
    nums = list(map(int, input().strip().split()))

    if X not in nums:
        result = False
        break

print('YES' if result else 'NO')
