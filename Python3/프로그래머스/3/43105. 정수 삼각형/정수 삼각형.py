def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    
    dp[0][0] = triangle[0][0]
    
    for i in range(1, len(triangle)):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == len(dp[i])-1:
                dp[i][j] = dp[i-1][len(dp[i])-2] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
    return max(dp[len(triangle)-1])
            
        