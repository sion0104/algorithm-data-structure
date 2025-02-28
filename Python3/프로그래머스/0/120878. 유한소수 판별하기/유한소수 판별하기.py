import math

def solution(a, b):
    gcd = math.gcd(a, b)    
    
    b_remainder = b // gcd
    
    while b_remainder % 2 == 0:
        b_remainder //= 2
    
    while b_remainder % 5 == 0:
        b_remainder //= 5
        
    
    if b_remainder == 1:
        return 1
    
    return 2