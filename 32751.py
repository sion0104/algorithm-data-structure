import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A, B, C, D = map(int, input().rstrip().split())
hamburger = deque(list(input().rstrip()))

result = True

for i in range(0, N - 1):
    if hamburger[i] == hamburger[i + 1]:
        result = False
        break

if hamburger[0] != 'a' or hamburger[-1] != 'a':
    result = False

if hamburger.count('a') > A or hamburger.count('b') > B or hamburger.count('c') > C or hamburger.count('D') > D:
    result = False

print('Yes ' if result else 'No')
