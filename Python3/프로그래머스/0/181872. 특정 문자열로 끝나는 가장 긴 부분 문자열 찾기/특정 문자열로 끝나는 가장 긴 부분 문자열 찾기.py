def solution(myString, pat):
    for index in range(len(myString), len(pat)-1, -1):
        subString = myString[0:index]
        if subString.endswith(pat):
            return subString
    
    return ""
    
    