import sys


def dfs(start):
    if len(S) == M:
        print('   '.join(map(str, S)))
        return
    for i in range(start, N + 1):
        if i not in S:
            S.append(i)
            dfs(i + 1)
            S.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
S = []
dfs(1)
