import sys
import math

prime = [True for _ in range(1235000)]
prime[1] = False
for i in range(2, int(math.sqrt(1235000)) + 1):
    if prime[i] is False:
        continue
    j = i + i
    while j < 1235000:
        prime[j] = False
        j += i

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ans = 0
    for i in range(n + 1, 2 * n + 1):
        if prime[i]:
            ans += 1
    print(ans)