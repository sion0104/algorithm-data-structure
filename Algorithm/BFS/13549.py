from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
MAX = 10 ** 5
visited = [0] * (MAX + 1)


def bfs(start, dest):
    queue = deque([start])

    while queue:
        location = queue.popleft()

        if location == dest:
            return  # 함수 종료

        for n_location in (2 * location, location - 1, location + 1):
            if n_location < 0 or n_location > MAX:
                continue
            if visited[n_location]:
                continue

            if n_location == 2 * location:
                visited[n_location] = visited[location]
            else:
                visited[n_location] = visited[location] + 1

            queue.append(n_location)


bfs(start=N, dest=K)
print(visited[K])
