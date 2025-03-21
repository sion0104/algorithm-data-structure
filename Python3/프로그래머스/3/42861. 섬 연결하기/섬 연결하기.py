def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    
def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    total_cost = 0
    bridge = 0
    
    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            bridge += 1
            
            if bridge == n - 1:
                break
    return total_cost