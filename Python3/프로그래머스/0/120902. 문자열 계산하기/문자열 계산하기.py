def solution(my_string):
    operation_list = my_string.split(" ")
    
    num1, num2 = int(operation_list[0]), int(operation_list[2])
    
    answer = int(operation_list[0])
    for index in range(1, len(operation_list), 2):
        num = int(operation_list[index + 1])
        
        if operation_list[index] == "+":
            answer += num
        else:
            answer -= num
            
    return answer