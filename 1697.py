from collections import deque
import sys


def BFS():
    queue = deque()
    queue.append(N)
    while queue:
        num = queue.popleft()
        if num == K:
            print(depth[num])
            break

        for num_next in (num - 1, num + 1, num * 2):
            if 0 <= num_next <= MAX and not depth[num_next]:
                depth[num_next] = depth[num] + 1
                queue.append(num_next)


MAX = 10 ** 5
depth = [0] * (MAX + 1)
N, K = map(int, sys.stdin.readline().split())

BFS()