import sys

input = sys.stdin.readline

A = 1
temp = 0
for _ in range(3):
    temp = int(input())
    A *= temp

result = str(A)

for i in range(0, 10):
    print(result.count(str(i)))