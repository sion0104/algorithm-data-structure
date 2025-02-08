def solution(n, k):
    price = n * 12000 + k * 2000
    
    service = n // 10
    if service > 0:
        price -= service * 2000
        
    return price