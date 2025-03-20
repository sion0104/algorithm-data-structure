# 번호: 1~n번
# 방향 그래프
def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for winner, loser in results:
        graph[winner][loser] = 1
        graph[loser][winner] = -1
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
    count = 0
    
    for i in range(1, n+1):
        known_matches = sum(1 for j in range(1, n+1) if graph[i][j] != 0 and j != i)
        if known_matches == n - 1:
            count += 1
            
    return count