# 정확하게 순위를 매길 수 있는 선수의 수
def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        graph[a][b] = 1 
        graph[b][a] = -1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    
    count = 0
    for i in range(1, n+1):
        know_matches = sum(1 for j in range(1, n+1) if graph[i][j] != 0 and j != i)
        if know_matches == n-1:
            count += 1
            
    return count
                    
        