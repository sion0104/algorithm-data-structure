def solution(my_string, target):
    answer = 0
    
    for i in range(0, len(my_string) - len(target) + 1):
        temp = my_string[i:i+len(target)]
        
        if temp == target:
            answer = 1
            
    return answer