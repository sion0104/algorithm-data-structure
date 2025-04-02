import sys
sys.setrecursionlimit(int(1e6))  # 재귀 제한 설정

def find_root(links):
    # 트리의 루트 노드를 찾는 함수
    length = len(links)
    visited = [False]*length  # 방문 여부를 체크하는 배열
    
    # 모든 노드를 순회하면서
    for i in range(length):
        if not visited[i]:  # 아직 방문하지 않은 노드를 발견하면
            result = i      # 해당 노드를 일단 결과값으로 저장
            q = [i]         # BFS를 위한 큐 초기화
            visited[i] = True
            
            # BFS로 연결된 모든 노드 방문
            while q:
                node = q.pop()
                for leaf in links[node]:  # 현재 노드의 자식들 확인
                    # 자식이 존재하고(-1이 아님) 아직 방문하지 않았다면
                    if leaf > -1 and not visited[leaf]:
                        visited[leaf] = True
                        q.append(leaf)
    
    return result  # 마지막으로 발견된 노드가 루트
    
def search(node, target, num, links):
    # 각 노드에서 가능한 그룹 분할을 탐색하는 함수
    # 반환값: (분할 횟수, 현재 그룹의 합)
    if node == -1:  # 리프 노드를 지났을 경우
        return 0, 0
    
    # 현재 노드의 왼쪽, 오른쪽 자식
    left, right = links[node]
    
    # 왼쪽, 오른쪽 서브트리 각각 재귀적으로 탐색
    left_cnt, left_val = search(left, target, num, links)
    right_cnt, right_val = search(right, target, num, links)
    tot_cnt = left_cnt + right_cnt  # 전체 분할 횟수
    
    # 현재 노드를 포함한 전체 서브트리의 합
    result_sum = left_val + right_val + num[node]
    
    # Case 1: 모든 값을 하나의 그룹으로 합칠 수 있는 경우
    if result_sum <= target:
        return tot_cnt, result_sum
    
    # Case 2: 현재 노드와 왼쪽/오른쪽 중 작은 쪽만 합치는 경우
    if min(left_val, right_val) + num[node] <= target:
        return tot_cnt + 1, min(left_val, right_val) + num[node]
    
    # Case 3: 현재 노드만 독립적인 그룹으로 분리해야 하는 경우
    return tot_cnt + 2, num[node]

def binary_search(root, start, end, k, num, links):
    # 이진 탐색으로 최적의 그룹 크기를 찾는 함수
    result = end  # 최소값을 찾아야 하므로 최댓값으로 초기화
    
    while start <= end:
        mid = (start + end) // 2
        # 현재 mid값으로 가능한 분할 횟수 확인
        div_cnt, _ = search(root, mid, num, links)
        
        if div_cnt > k-1:  # 분할 횟수가 너무 많으면
            start = mid+1   # 그룹의 크기를 늘려야 함
        else:              # 분할 횟수가 k-1 이하면
            result = min(result, mid)  # 현재값 저장
            end = mid-1    # 더 작은 그룹 크기 시도
    
    return result
    
def solution(k, num, links):
    length = len(links)
    # 루트 노드 찾기
    root = find_root(links)
    
    # 이진 탐색의 범위 설정
    # 시작값: 개별 노드의 최댓값 (최소한 이 값 이상이어야 함)
    # 종료값: 모든 노드의 합 (이보다 클 수는 없음)
    start, end = max(num), sum(num)
    
    # 이진 탐색으로 최적의 값 찾기
    answer = binary_search(root, start, end, k, num, links)

    return answer