def solution(num_list):
    answer = [0, 0]
    
    for num in num_list:
        index = 0 if num % 2 == 0 else 1
        answer[index] += 1
        
    return answer