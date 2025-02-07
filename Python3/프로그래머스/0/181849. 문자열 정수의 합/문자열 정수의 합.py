def solution(num_str):
    answer = 0
    
    for char in num_str:
        num = int(char)
        
        answer += num
        
    return answer