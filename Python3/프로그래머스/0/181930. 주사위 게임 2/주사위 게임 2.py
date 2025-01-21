def solution(a, b, c):
    answer = a + b + c
    
    if a == b or b == c or a == c: 
        answer *= pow(a, 2) + pow(b, 2) + pow(c, 2)
        
    if a == b and b == c: 
        answer *= pow(a, 3) + pow(b, 3) + pow(c, 3)
        
    return answer