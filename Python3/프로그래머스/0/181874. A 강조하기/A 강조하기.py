def solution(myString):
    answer = ""
    
    for string in myString:
        if string == "a":
            answer += "A"
        elif string == "A":
            answer += string
        else:
            answer += string.lower()
    
    return answer