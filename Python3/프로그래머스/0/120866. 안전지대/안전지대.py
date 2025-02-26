def solution(board):
    n = len(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1) ]
    
    danger_zones = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                danger_zones[i][j] = 1
                
                for direction in directions:
                    ni, nj = i + direction[0], j + direction[1]
                    
                    if 0 <= ni < n and 0 <= nj < n:
                        danger_zones[ni][nj] = 1
                        
    safe_count = sum(danger_zones[i][j] == 0 for i in range(n) for j in range(n))
    
    return safe_count