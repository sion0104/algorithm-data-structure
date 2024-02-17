import sys


def quadTree(size, area):
    temp_sum = 0

    for line in area:
        temp_sum += sum(line)

    if temp_sum == size ** 2:
        return '1'
    if temp_sum == 0:
        return '0'

    half = size // 2
    temp = '('
    temp += quadTree(half, [row[:half] for row in area[:half]])
    temp += quadTree(half, [row[half:] for row in area[:half]])
    temp += quadTree(half, [row[:half] for row in area[half:]])
    temp += quadTree(half, [row[half:] for row in area[half:]])
    temp += ')'

    return temp


input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    line = list(map(int, input().rstrip()))
    lines.append(line)

print(quadTree(N, lines))
