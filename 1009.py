import sys

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    tmp_a = a % 10

    if tmp_a == 0:
        print(10)
    elif tmp_a in [1, 5, 6]:
        print(tmp_a)
    elif tmp_a in [4, 9]:
        tmp_b = b % 2
        print(tmp_a * tmp_a % 10) if tmp_b == 0 else print(tmp_a)
    else:
        tmp_b = b % 4
        print(tmp_a ** 4 % 10) if tmp_b == 0 else print(tmp_a ** tmp_b % 10)
