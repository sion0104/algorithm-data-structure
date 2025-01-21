def solution(numLog):
    answer = ''
    
    for i in range(len(numLog)-1):
        difference = numLog[i+1] - numLog[i]
        if difference == 1:
            answer += "w"
        elif difference == -1:
            answer += "s"
        elif difference == 10:
            answer += "d"
        else:
            answer+= "a"
            
    return answer