def solution(s):
    str_list = s.split()
    answer = 0
    
    for index in range(len(str_list)):
        if str_list[index] == "Z":
            str_list[index - 1] = "0"
    
    for index in range(len(str_list)):
        if str_list[index] == "Z":
            continue
            
        answer += int(str_list[index])
        
    return answer
            