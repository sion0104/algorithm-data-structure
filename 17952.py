import sys

input = sys.stdin.readline

N = int(input())
assignment, result = [], 0

for i in range(N):
    minute = list(map(int, input().split()))

    if minute[0] == 1:
        assignment.append((minute[1], minute[2]))

    if assignment:
        score, time = assignment.pop()
        time -= 1

        if time == 0:
            result += score
        else:
            assignment.append((score, time))

print(result)
