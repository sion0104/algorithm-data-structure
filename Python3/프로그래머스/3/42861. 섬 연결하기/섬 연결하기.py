def find_parent(parent, x):
    # 경로 압축을 통한 루트 노드 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 두 노드의 부모를 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    # 1. 비용순으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # 2. 부모 테이블 초기화
    parent = [i for i in range(n)]
    
    # 3. 결과 변수 초기화
    total_cost = 0
    bridges = 0  # 선택된 다리의 수
    
    # 4. 크루스칼 알고리즘 수행
    for a, b, cost in costs:
        # 사이클이 발생하지 않는 경우에만 선택
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total_cost += cost
            bridges += 1
            # 필요한 다리를 모두 선택했으면 종료
            if bridges == n - 1:
                break
    
    return total_cost