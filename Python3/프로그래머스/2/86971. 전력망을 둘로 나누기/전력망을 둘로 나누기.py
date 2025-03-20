# 송전탑의 개수, 전선 정보
def solution(n, wires):
    # 전선 중 하나를 끊어 네트워크 2개로 분할
    # 두 전력망의 송전탑 개수 최대한 비슷
    
    # 깊이 탐색(DFS)
    
    answer = n
    
    def dfs(start, visited):
        count = 1
        for v in graph[start]:
            if v not in visited:
                visited.add(v)
                count += dfs(v, visited)
        return count
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
    
        for j in range(len(wires)):
            if i != j:
                v1, v2 = wires[j]
                graph[v1].append(v2)
                graph[v2].append(v1)
        
        visited = {1}
        network1 = dfs(1, visited)
        network2 = n - network1
        
        answer = min(answer, abs(network1 - network2))
        
    return answer
        
    # 반환값: 송전탑 개수 차이(절대값)