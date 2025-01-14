import sys

input = sys.stdin.readline

N = int(input())

if N > 100000 or N < 2024 or N % 2024 != 0:
    print('No')
else:
    print('Yes')