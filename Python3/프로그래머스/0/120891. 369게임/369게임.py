def solution(order):
    clap = "369"
    
    answer = 0
    
    for char in str(order):
        if char in clap:
            answer += 1
    
    return answer