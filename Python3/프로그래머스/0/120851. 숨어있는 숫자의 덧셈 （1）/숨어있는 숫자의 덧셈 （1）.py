def solution(my_string):
    answer = 0
    for char in my_string:
        if char.isdecimal():
            answer += int(char)
            
    return answer