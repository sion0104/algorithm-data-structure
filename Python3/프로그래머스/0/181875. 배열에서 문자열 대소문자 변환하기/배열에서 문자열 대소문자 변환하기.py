def solution(strArr):
    answer = []
    
    for index in range(len(strArr)):
        if index % 2 == 0:
            answer.append(strArr[index].lower())
        else:
            answer.append(strArr[index].upper())
        
    return answer