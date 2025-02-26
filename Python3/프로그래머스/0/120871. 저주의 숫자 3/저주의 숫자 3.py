def solution(n):
    b = 4
    
    if n < 3:
        return n
    
    for i in range(4, n+1):
        b += 1
        while "3" in str(b) or b % 3 == 0:
            b += 1
        
        
    return b