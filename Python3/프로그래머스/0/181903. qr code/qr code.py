def solution(q, r, code):
    if q == 1:
        return code
    
    answer = ''
    
    for i in range(r,len(code),q):
        answer += code[i]
        
    return answer