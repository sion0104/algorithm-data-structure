def solution(polynomial):
    answer = [0, 0]
    elements = polynomial.split(" ")
    
    for element in elements:
        if "x" in element:
            if len(element) == 1:
                answer[0] += 1
                continue
            answer[0] += int(element[0:len(element) - 1])
        elif element == "+":
            continue
        else:
            answer[1] += int(element[0:len(element)])
    
    x_part = f"{answer[0]}x" if answer[0] != 1 else "x"
    if answer[0] == 0:
        return str(answer[1])
    elif answer[1] == 0:
        return x_part
    else:
        return f"{x_part} + {answer[1]}"