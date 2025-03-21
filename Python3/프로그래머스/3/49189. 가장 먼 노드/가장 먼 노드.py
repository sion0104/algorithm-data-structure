from collections import deque

def solution(n, edge):
    graph = [[] * (n+1) for _ in range(n+1)]
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    queue = deque([(1, 0)])
    visited = [False] * (n + 1)
    distance = [0] * (n+1)
    
    visited[1] = True
    max_depth = 0
    
    while queue:
        current, depth = queue.popleft()
        
        max_depth = max(max_depth, depth)
        
        for next_node in graph[current]:
            if not visited[next_node]:
                queue.append((next_node, depth + 1))
                visited[next_node] = True
                distance[next_node] = depth + 1
                
    return distance.count(max_depth)
                
            