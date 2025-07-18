def solution(s):
    result = ""
    wordIndex = -1
    
    for char in s:
        if char == " ":
            result += char
            wordIndex = -1
        else:
            wordIndex += 1
            
            if wordIndex % 2 == 0:
                result += char.upper()
            else:
                result += char.lower()
                
    
    return result