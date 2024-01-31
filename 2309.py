import sys

height = []
for _ in range(9):
    height.append(int(sys.stdin.readline()))

height.sort()
height_sum = sum(height)

for i in range(len(height)):
    for j in range(i+1, len(height)):
        if height_sum - (height[i] + height[j]) == 100:
            for k in range(len(height)):
                if k == i or k == j:
                    continue
                else:
                    print(height[k])
            exit()
