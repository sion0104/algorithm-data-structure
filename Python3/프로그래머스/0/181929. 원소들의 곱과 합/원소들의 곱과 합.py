def solution(num_list):
    multiply, sum = 1, 0
    
    for i in num_list:
        multiply *= i
        sum += i
        
    return 1 if multiply < pow(sum, 2) else 0
        