import sys

input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))
sorted_A = sorted(A[L-1:R])

if (L > 1 and sorted_A[0] < A[L-2]) or (R < N and sorted_A[-1] > A[R]):
    print(0)
else:
    print(1)
