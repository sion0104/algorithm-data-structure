import sys

input = sys.stdin.readline

def max_triangles(sticks):
    sticks.sort()
    n = len(sticks)
    count = 0

    for i in range(n-1, 1, -1):
        c = sticks[i]
        a, b = 0, i - 1
        while a < b:
            if sticks[a] + sticks[b] > c:
                count += b-a
                b -= 1
            else:
                a += 1

    return count

N = int(input())
sticks = list(map(int, input().split()))
print(max_triangles(sticks))
