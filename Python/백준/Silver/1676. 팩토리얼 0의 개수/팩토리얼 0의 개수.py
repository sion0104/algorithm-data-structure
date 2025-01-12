import sys
import math

input = sys.stdin.readline

N = int(input())

factorial = list(str(math.factorial(N)))
factorial.reverse()

count = 0
for i in factorial:
    if i == '0':
        count += 1
    else:
        break

print(count)
