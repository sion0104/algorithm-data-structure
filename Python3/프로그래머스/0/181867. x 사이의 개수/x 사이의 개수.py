def solution(myString):
    parts = myString.split("x")
    
    lengths = [len(part) for part in parts ]
    
    return lengths