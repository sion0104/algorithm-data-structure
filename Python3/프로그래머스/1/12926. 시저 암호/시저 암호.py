def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += ' '
        elif char.isupper():
            num = ord(char)
            for i in range(n):
                num += 1
                if num > ord('Z'):
                    num = ord('A')
            answer += chr(num)
        else:
            num = ord(char)
            for i in range(n):
                num += 1
                if num > ord('z'):
                    num = ord('a')
            answer += chr(num)
                    
    return answer