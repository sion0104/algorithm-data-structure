import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())
count = 0

while N > 1:
    size = (2 ** N) // 2

    if r < size and c < size:
        pass
    elif r < size <= c:
        count += size ** 2
        c -= size
    elif r >= size > c:
        count += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        count += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(count)
if r == 0 and c == 1:
    print(count + 1)
if r == 1 and c == 0:
    print(count + 2)
if r == 1 and c == 1:
    print(count + 3)
