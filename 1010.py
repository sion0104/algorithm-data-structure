import sys

input = sys.stdin.readline

T = int(input())

dp = [[0]*30 for _ in range(30)]
dp[0] = [i for i in range(1, 31)]

for i in range(1, 30):
    for j in range(1, 30):
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(T):
    N, M = map(int, input().split())
    print(dp[N-1][M-1])
