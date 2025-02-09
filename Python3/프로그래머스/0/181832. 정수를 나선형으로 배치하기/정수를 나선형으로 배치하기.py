def solution(n):
    matrix = [[0]*n for _ in range(n)]
    
    # 오른쪽, 아래, 왼쪽, 위
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0
    
    row, col = 0, 0
    for num in range(1, n**2 + 1):
        matrix[row][col] = num
        
        next_row = row + directions[direction_index][0]
        next_col = col + directions[direction_index][1]
        
        if not(0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            direction_index = (direction_index + 1) % 4
            next_row = row + directions[direction_index][0]
            next_col = col + directions[direction_index][1]
        
        row, col = next_row, next_col
        
    return matrix
        
    