import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = sys.stdin.readline()

    number = int(N[-3:])
    year = int(N)+1

    if year % number == 0:
        print('Good')
    else:
        print('Bye')
