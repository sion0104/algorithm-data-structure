def solution(l, r):
    answer = []
    
    def generateNumber(current):
        number = int(current)
        
        if l <= number <= r:
            answer.append(number)
        if number > r:
            return
        
        generateNumber(current + "0")
        generateNumber(current + "5")
    
    generateNumber("5")
    
    answer.sort()
            
    return answer if answer else [-1]