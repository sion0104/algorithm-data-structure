def solution(code):
    mode = True
    ret = ''
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
            continue
            
            
        if mode == True and i % 2 == 0:
            ret += code[i]
        elif mode == False and i % 2 != 0:
            ret += code[i]
            
    if ret == '':
        return "EMPTY"
    
    return ret