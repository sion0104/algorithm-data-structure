def solution(x):
    str_x = str(x)
    
    num = 0
    for i in str_x:
        num += int(i)
        
    return True if x % num == 0 else False