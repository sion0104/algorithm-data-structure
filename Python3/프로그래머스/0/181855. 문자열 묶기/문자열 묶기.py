def solution(strArr):
    num_count = {}
    
    for string in strArr:
        length = len(string)
        
        if length not in num_count:
            num_count[length] = 1
        else:
            num_count[length] += 1
            
    
    return max(num_count.values())