def solution(num, k):
    answer = -1
    num_list = list(str(num))
    
    for index in range(len(num_list)):
        if num_list[index] == str(k):
            answer = index + 1
            break
            
    return answer