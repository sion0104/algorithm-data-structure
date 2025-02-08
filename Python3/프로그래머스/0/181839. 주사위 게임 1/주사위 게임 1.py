def solution(a, b):
    numA, numB = a % 2, b % 2
    
    if numA + numB == 2:
        return int(pow(a, 2) + pow(b, 2))
    elif numA + numB == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)