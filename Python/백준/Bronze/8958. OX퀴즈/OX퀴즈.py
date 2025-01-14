import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    corrects = list(map(str, input().rstrip().split('X')))

    score = 0
    for correct in corrects:
        for i in range(1, len(correct)+1):
            score += i
    print(score)
