def solution(n):
    answer = []
    
    num = n
    
    while num != 1:
        answer.append(num)
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    
    answer.append(1)
        
    return answer