def solution(num_list, n):
    answer = []
    row_count = len(num_list) // n
    
    for i in range(row_count):
        row = num_list[i*n:(i+1)*n]
        answer.append(row)
    
    return answer
    