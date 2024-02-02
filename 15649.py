import sys


def DFS():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        array.append(i)
        DFS()
        array.pop()
        visited[i] = False


N, M = map(int, sys.stdin.readline().split())
array = []
visited = [False] * (N + 1)

DFS()
