def solution(picture, k):
    answer = []
    
    for line in picture:
        pixels = ""
        
        for pixel in line:
            pixels += pixel * k
            
        for _ in range(k):
            answer.append(pixels)
            
    return answer