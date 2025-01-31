def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    commonDenom = denom1 * denom2
    numeratorSum = numer1 * denom2 + numer2 * denom1
    
    divisor = gcd(numeratorSum, commonDenom)
    
    return [numeratorSum // divisor, commonDenom // divisor]