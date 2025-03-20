from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    number_set = set()
    
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i))
        
        for perm in perms:
            num = int(''.join(perm))
            number_set.add(num)
            
    for num in number_set:
        if is_prime(num):
            answer += 1
            
    return answer