import math

def solution(arr):
    n = len(arr)
    
    next_power_of_two = 2**math.ceil(math.log2(n))
    
    while len(arr) < next_power_of_two:
        arr.append(0)
        
    return arr
        
    