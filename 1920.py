import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

for num in array:
    print(1) if num in A else print(0)

# set 사용해 중복 제거 후, 탐색
