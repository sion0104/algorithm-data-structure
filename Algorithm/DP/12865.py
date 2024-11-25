# 가방 채우기

import sys

input = sys.stdin.readline

# 물건의 개수, 가방 최대 무게
N, K = map(int, input().split())

# ([물건의 무게][물건의 가치]) * 물건의 개수 : 2차원 배열
bag = [list(map(int, input().split())) for _ in range(N)]

# dp 배열
# 이전의 무게를 이용
# 따라서 첫번째 물건을 위한 행 첫 번째는 모두 0으로 구성.
# 가방 무게 별에 따른 물건의 최대 가치 저장
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j >= bag[i - 1][0]:  # 가방의 무게(j)가 현재 물건의 무게(bag[i-1][0])보다 큰 경우
            # 현재의 가방의 무게에서 이전 물건을 담은 경우의 가치 / 현재 가방의 무게에서 현재 물건의 가치 + 남은 무게에 대한 가치 최댓값 중에 큰 값
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bag[i - 1][0]] + bag[i - 1][1])
        else:
            dp[i][j] = dp[i - 1][j]

# 항상 끝의 부분이 정답
print(dp[N][K])
