import sys

N = int(sys.stdin.readline())

result = list(sys.stdin.readline().rstrip())

for i in range(N-1):
    line = list(sys.stdin.readline().rstrip())
    for j in range(len(result)):
        if result[j] != line[j]:
            result[j] = '?'

print(''.join(result))
