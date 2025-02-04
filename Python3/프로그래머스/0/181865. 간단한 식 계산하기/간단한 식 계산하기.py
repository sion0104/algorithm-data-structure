def solution(binomial):
    a_str, operation, b_str = binomial.split(" ")
    
    a, b = int(a_str), int(b_str)
    
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    else:
        return a * b