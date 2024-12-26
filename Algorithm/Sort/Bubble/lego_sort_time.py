import sys

input = sys.stdin.readline

def logo_assembly_time(n, sizes):
    total_time = 0
    swapped = True

    while swapped:
        swapped = False
        for i in range(n-1):
            if sizes[i] > sizes[i+1]:
                total_time += abs(sizes[i]-sizes[i+1])
                swapped = True

        n -= 1

    return total_time

N = int(input())
sizes = list(map(int, input().split()))
print(logo_assembly_time(N, sizes))
