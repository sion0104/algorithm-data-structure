def solution(myString, pat):
    transformed = myString.translate(str.maketrans("AB", "BA"))
    
    return 1 if pat in transformed else 0
