def is_composite_number(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def solution(n):
    count = 0
    for i in range(1, n+1):
        if is_composite_number(i):
            count += 1
    return count