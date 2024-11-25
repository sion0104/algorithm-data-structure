import sys
import queue

input = sys.stdin.readline

N = int(input())

queue = queue.Queue()


def execution(command):
    if command[0] == 'push':
        queue.put(int(command[1]))
    elif command[0] == 'pop':
        if queue.qsize() <= 0:
            print(-1)
        else:
            print(queue.get())
    elif command[0] == 'size':
        print(queue.qsize())
    elif command[0] == 'empty':
        if queue.qsize() <= 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue.qsize() <= 0:
            print(-1)
        else:
            print(queue.queue[0])
    else:
        if queue.qsize() <= 0:
            print(-1)
        else:
            print(queue.queue[-1])


for _ in range(N):
    command = list(input().split())
    execution(command)

# queue 라이브러리는 메모리에 대한 강점
# deque는 시간에 대한 강점
