def solution(chicken):
    chickens = chicken // 10
    coupons = chicken % 10
    
    prev_chickens = chickens
    while True:
        coupons += prev_chickens
        
        chickens += coupons // 10
        
        prev_chickens = coupons // 10
        coupons = coupons % 10 
        
        if prev_chickens + coupons < 10:
            break
    
    return chickens
        