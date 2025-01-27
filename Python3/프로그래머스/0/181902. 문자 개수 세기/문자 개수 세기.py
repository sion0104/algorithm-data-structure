def solution(my_string):
    answer = [0 for _ in range(52)]
    
    for char in my_string:
        char_int = ord(char)
        if 65 <= char_int <= 90:
            answer[char_int-65] += 1
        else:
            answer[char_int-71] += 1
    
    return answer