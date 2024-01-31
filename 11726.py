import sys

n = int(sys.stdin.readline())

result = [0, 1, 2]

for i in range(3, n + 1):
    result.append((result[i - 2] + result[i - 1]) % 10007)

print(result[n])
