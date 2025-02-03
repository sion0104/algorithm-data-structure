def solution(strArr):
    answer = []
    
    for index in range(len(strArr)):
        string = strArr[index]
        
        if "ad" not in string:
            answer.append(string)
            
    return answer