from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    bridge_weight = 0
    time = 0
    
    # 첫 트럭 진입
    if trucks:
        truck = trucks.popleft()
        bridge[-1] = truck
        bridge_weight += truck
    
    while bridge_weight > 0:  # 다리 위에 트럭이 있는 동안만 반복
        time += 1
        
        # 다리에서 트럭 빼기
        bridge_weight -= bridge[0]
        bridge.popleft()
        
        # 새 트럭 추가 가능한지 확인
        if trucks and bridge_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)
    
    return time + 1  # 마지막 트럭이 다리를 완전히 건너는 시간 추가
