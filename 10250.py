import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    height, weight, num = map(int, input().split())

    floor = num % height
    room = (num // height) + 1
    if floor == 0:
        floor = height
        room -= 1

    print(floor * 100 + room)
