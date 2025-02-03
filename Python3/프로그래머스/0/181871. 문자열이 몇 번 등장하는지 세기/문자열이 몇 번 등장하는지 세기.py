def solution(myString, pat):
    answer = 0
    for index in range(len(myString)-len(pat)+1):
        subString = myString[index: index+len(pat)]
        if subString == pat:
            answer += 1
    
    return answer