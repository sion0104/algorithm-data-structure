import sys

N = int(sys.stdin.readline())
F = int(sys.stdin.readline())

result = (N // 100) * 100

while result % F != 0:
    result += 1
print(str(result)[-2:])