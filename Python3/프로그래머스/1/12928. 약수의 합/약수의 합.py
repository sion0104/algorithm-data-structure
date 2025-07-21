def solution(n):
    if n == 0 or n == 1:
        return n
    
    answer = 1
    
    for i in range(2, n // 2 + 1, 1):
        if n % i == 0:
            answer += i
            
    return answer + n