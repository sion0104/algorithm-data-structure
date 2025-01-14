import sys

input = sys.stdin.readline

L = int(input())
chars = input()

result = 0

for l in range(L):
    result += (ord(chars[l])-ord('a') + 1) * (31 ** l)

print(result % 1234567891)
