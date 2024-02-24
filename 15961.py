import sys
from collections import defaultdict

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

sushi.extend(sushi)

left, right, result = 0, 0, 0
dictionary = defaultdict(int)

dictionary[c] += 1

while right < k:
    dictionary[sushi[right]] += 1
    right += 1

while right < len(sushi):
    result = max(result, len(dictionary))

    dictionary[sushi[left]] -= 1
    if dictionary[sushi[left]] == 0:
        del dictionary[sushi[left]]

    dictionary[sushi[right]] += 1

    left += 1
    right += 1

print(result)
