def solution(num, total):
    answer = []
    
    start_num, middle_index = total // num, 0
    if num % 2 == 0:
        middle_index = num // 2 - 1
    else:
        middle_index = num // 2
    
    for i in range(num):
        answer.append(start_num - middle_index + i)
    
    return answer    