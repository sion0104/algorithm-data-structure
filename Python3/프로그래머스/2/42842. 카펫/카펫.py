def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
        
    for i in range(1, yellow//2 + 1):
        if yellow % i != 0:
            continue
            
        width, height = yellow // i, i
        
        brown_count = (width + 2) * 2 + height * 2
        
        if brown_count == brown:
            return [width + 2, height + 2]