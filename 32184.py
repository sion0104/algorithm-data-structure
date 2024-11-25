import sys

input = sys.stdin.readline

A, B = map(int, input().split())

result = 0
current_page = A

while current_page <= B:
    result += 1
    if current_page % 2 == 1:
        current_page += 1
    current_page += 1

print(result)