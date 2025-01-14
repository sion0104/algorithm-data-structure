import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n + 1)]


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    operation, a, b = map(int, input().rstrip().split())
    if operation == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
