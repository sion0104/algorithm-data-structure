def solution(n):
    answer = 2
    
    while answer <= n//2:
        if n % answer == 1:
            return answer
        answer += 1
        
    return n - 1