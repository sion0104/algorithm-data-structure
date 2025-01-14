import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
reverse_A = A[::-1]

increase_dp = [1] * (N)
decrease_dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j]+1)
        if reverse_A[i] > reverse_A[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j]+1)

decrease_dp = decrease_dp[::-1]

result = list()
for i in range(N):
    result.append(increase_dp[i] + decrease_dp[i]-1)

print(max(result))
