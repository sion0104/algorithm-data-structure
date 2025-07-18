def solution(price, money, count):
    sum = 0
    
    for i in range(1, count+1):
        sum += i
        
    if money > price * sum:
        return 0
    else:
        return price * sum - money