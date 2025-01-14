import sys

input = sys.stdin.readline

x = int(input())
x -= 1

if x % 3 == 0:
    print('U')
elif x % 3 == 1:
    print('O')
else:
    print('S')
