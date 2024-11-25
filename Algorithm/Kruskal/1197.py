import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
V, E = map(int, input().split())

edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

parent = [i for i in range(V + 1)]


def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


total_cost = 0

for edge in edges:
    C, A, B = edge
    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        total_cost += C

print(total_cost)
