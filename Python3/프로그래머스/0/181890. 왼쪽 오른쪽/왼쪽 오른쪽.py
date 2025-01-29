def solution(str_list):
    answer = []
    
    for index in range(len(str_list)):
        if str_list[index] == "l":
            answer = str_list[0:index]
            break
        elif str_list[index] == "r":
            answer = str_list[index+1:]
            break
            
    return answer