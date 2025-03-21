# 정해진 순서로(queue) 다리 건너기
# 반환값: 모든 트럭이 다리를 건너기 위한 최소 시간

# 최대 다리에 올라갈 수 있는 트럭의 개수, 다리에 올라갈 수 있는 최대 무게, 트럭 무게 배열
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    
    bridge_weight = 0
    time = 0
    
    if trucks:
        truck = trucks.popleft()
        bridge_weight += truck
        bridge[-1] = truck
        
    while bridge_weight > 0:
        time += 1
        
        bridge_weight -= bridge[0]
        bridge.popleft()
        
        if trucks and trucks[0] + bridge_weight <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:
            bridge.append(0)
            
    return time + 1
        