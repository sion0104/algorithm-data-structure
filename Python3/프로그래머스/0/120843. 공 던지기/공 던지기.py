def solution(numbers, k):
    answer = 0
    count = len(numbers)
    
    for index in range(k-1):
        answer += 2
        
        if answer >= count:
            answer = answer % count
        
    return numbers[answer]