def solution(emergency):
    sorted_emergency = sorted(enumerate(emergency), key=lambda x: -x[1])
    
    result = [0] * len(emergency)
    
    for order, (index, _) in enumerate(sorted_emergency):
        result[index] = order + 1
        
    return result