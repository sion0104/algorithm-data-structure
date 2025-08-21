def solution(numbers):
    zero_to_nine = set([i for i in range(0, 10)])
    
    answer = zero_to_nine - set(numbers)
    
    return sum(answer)