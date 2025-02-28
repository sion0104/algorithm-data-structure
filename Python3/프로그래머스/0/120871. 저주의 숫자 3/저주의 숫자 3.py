def solution(n):
    number, result = 0, 0

    for _ in range(1, n+1):
        number += 1
        
        while number % 3 == 0 or "3" in str(number):
            number += 1
        
        result = number
        
    return result