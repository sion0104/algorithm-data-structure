def solution(numbers):
    numbers.sort()
    
    max_product1 = numbers[-1] * numbers[-2]
    max_product2 = numbers[0] * numbers[1]
    
    return max(max_product1, max_product2)