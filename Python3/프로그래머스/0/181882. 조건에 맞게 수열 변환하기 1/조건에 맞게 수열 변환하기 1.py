def solution(arr):
    answer = []
    
    for index in range(len(arr)):
        num = arr[index]
        if num >= 50 and num % 2 == 0:
            num /= 2
        elif num < 50 and num % 2 != 0:
            num *= 2
        
        answer.append(num)
        
    return answer