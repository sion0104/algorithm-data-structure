def solution(n):
    n_list = list(str(n))
    
    answer = 0
    for char in n_list:
        num = int(char)
        answer += num
        
    return answer