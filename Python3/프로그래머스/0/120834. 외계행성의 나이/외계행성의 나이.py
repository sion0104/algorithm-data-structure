def solution(age):
    alphabet = "abcdefghij"
    
    age_str = str(age)
    result = ""
    
    for digit in age_str:
        result += alphabet[int(digit)]
    
    return result
            