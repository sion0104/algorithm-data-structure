def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        if count_divisor(i) % 2 == 0:
            result += i
        else:
            result -= i
    
    return result

def count_divisor(num):
    if num <= 0:
        return 0
    
    divisor_count = 1
    i = 2
    
    while i * i <= num:
        count = 0
        while num % i == 0:
            count += 1
            num //= i
        
        divisor_count *= (count + 1)
        i += 1
        
    if num > 1:
        divisor_count *= 2
    
    return divisor_count
            