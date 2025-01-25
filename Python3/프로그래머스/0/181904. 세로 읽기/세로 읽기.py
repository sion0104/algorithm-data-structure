def solution(my_string, m, c):
    if m == 1:
        return my_string 
    
    answer = ""
    for i in range(c-1, len(my_string), m):
        answer += my_string[i]
    
    return answer