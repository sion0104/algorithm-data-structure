import sys

input = sys.stdin.readline

N = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())

left, right = 0, N - 1
result = 0

while left < right:
    sum = nums[left] + nums[right]

    if sum == x:
        result += 1
        left += 1
    elif sum > x:
        right -= 1
    else:
        left += 1

print(result)
