import sys

input = sys.stdin.readline

N = int(input())

result = False
for i in range(2, 10):
    if 0 < N < 10:
        result = True
        break
    if N % i == 0 and 0 < N // i < 10:
        result = True
        break

print(1 if result else 0)
