from collections import deque

# 직사각형(2차원배열), 초기 캐릭터 위치(x, y), 아이쳄 위치(x, y)
def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[0] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 2
                elif field[i][j] != 2:
                    field[i][j] = 1
                    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    queue = deque([(characterX, characterY, 0)])
    visited = set([(characterX, characterY)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == itemX and y == itemY:
            # 반환값: 최소 거리
            return distance // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 102 and 0 <= ny < 102:
                if (nx, ny) not in visited and field[nx][ny] == 1:
                    queue.append((nx, ny, distance + 1))
                    visited.add((nx, ny))
            
    return 0
    
    
  