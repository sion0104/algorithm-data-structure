import sys

input = sys.stdin.readline

N, M = map(int, input().split())
relations = [[] for _ in range(N)]
visited, answer = [False] * 2001, False

for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(idx, depth):
    global answer
    visited[idx] = True

    if depth == 4:
        answer = True
        return

    for i in relations[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False


for i in range(N):
    dfs(i, 0)
    visited[i] = False

    if answer:
        break

print(1) if answer else print(0)
