def solution(a, b):
    answer = 0
    
    option1 = a * pow(10, len(str(b))) + b
    
    answer = max(option1, 2 * a * b)
    
    return answer