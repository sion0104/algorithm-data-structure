import sys

input = sys.stdin.readline

nums = list(map(int, input().split()))

if nums == [i for i in range(1, 9)]:
    print('ascending')
elif nums == [i for i in range(8, 0, -1)]:
    print('descending')
else:
    print('mixed')
