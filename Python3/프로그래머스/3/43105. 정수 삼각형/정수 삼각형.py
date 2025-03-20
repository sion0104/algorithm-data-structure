def solution(triangle):
    height = len(triangle)
    dp = [[0] * len(row) for row in triangle]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, height):
        for j in range(len(triangle[i])):
            current = triangle[i][j]
            
            if j == 0:
                dp[i][j] = dp[i-1][j] + current
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j-1] + current
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + current
    
    return max(dp[-1])