def solution(arr):    
    count = 0
    
    while True:
        temp = []
        
        for num in arr:
            if num >= 50 and num % 2 == 0:
                temp.append(num // 2)
            elif num < 50 and num % 2 != 0:
                temp.append(num * 2 + 1)
            else:
                temp.append(num)
        
        
        if temp == arr:
            return count
        
        arr = temp
        count += 1
        