import math

prime = [True for _ in range(1000000+1)]
prime[0], prime[1] = False, False

for i in range(2, int(math.sqrt(1000000))+1):
    if prime[i]:
        j = 2
        while j * i <= 1000000:
            prime[i*j] = False
            j += 1

T = int(input())
for i in range(T):
    N = int(input())

    result = 0
    for i in range(2, int(N/2)+1):
        if prime[i] == False or prime[N-i] == False:
            continue

        result += 1
    print(result)