import sys

input = sys.stdin.readline

N = int(input())
visited = [-1] * N
count = 0


def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or abs(now_row - row) == abs(visited[now_row] - visited[row]):
            return False
    return True


def dfs(row):
    global count

    if row == N:
        count += 1
    else:
        for col in range(N):
            visited[row] = col
            if check(row):
                dfs(row + 1)


dfs(0)
print(count)
