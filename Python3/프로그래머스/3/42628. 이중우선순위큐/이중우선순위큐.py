# 연산 배열
# 큐가 비어 있으면 [0, 0], [최댓값, 최솟값] 반환
import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    number_dict = {}
    
    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)
        
        if alphabet == "I":
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            number_dict[number] = number_dict.get(number, 0) + 1
            
        else:
            if not number_dict:
                continue
                
            if number == 1:
                while max_heap:
                    max_val = -1 * heapq.heappop(max_heap)
                    
                    if number_dict.get(max_val, 0) > 0:
                        number_dict[max_val] -= 1
                        if number_dict[max_val] == 0:
                            del number_dict[max_val]
                        break
            else:
                while min_heap:
                    min_val = heapq.heappop(min_heap)
                    
                    if number_dict.get(min_val, 0) > 0:
                        number_dict[min_val] -= 1
                        if number_dict[min_val] == 0:
                            del number_dict[min_val]
                        break
                        
    if not number_dict:
        return [0, 0]
    
    max_val = max(number_dict.keys())
    min_val = min(number_dict.keys())
    
    return [max_val, min_val]
