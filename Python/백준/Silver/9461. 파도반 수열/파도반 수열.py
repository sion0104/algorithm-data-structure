import sys

# f(n) = f(n-2) + f(n-3) (단, n = 1, 2, 3일때 f(n) = 1)

input = sys.stdin.readline

T = int(input())
array = [-1 for _ in range(101)]

for i in range(1, 101):
    if 0 < i < 4:
        array[i] = 1
        continue

    array[i] = array[i-2] + array[i-3]

for _ in range(T):
    N = int(input())
    print(array[N])