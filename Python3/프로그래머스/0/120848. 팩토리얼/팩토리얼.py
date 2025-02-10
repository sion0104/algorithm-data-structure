def solution(n):
    i, factorial = 1, 1
    
    while factorial <= n:
        i += 1
        factorial *= i
        
    return i-1
    
    