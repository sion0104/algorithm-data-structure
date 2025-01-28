def solution(num_list):
    
    for index in range(len(num_list)):
        if num_list[index] < 0:
            return index
        
    return -1