def solution(a, b):
    answer = 0
    
    if a * (10 ** len(str(b))) + b > a + b * (10 ** len(str(a))):
        answer = a * (10 ** len(str(b))) + b
    else :
        answer = a + b * (10 ** len(str(a)))
    return answer