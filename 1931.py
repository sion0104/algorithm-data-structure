import sys

N = int(sys.stdin.readline())
time = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time.append((start, end))

time.sort(key=lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)
