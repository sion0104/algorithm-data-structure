import sys


def switch(number):
    if switches[number] == 0:
        switches[number] = 1
    else:
        switches[number] = 0


count = int(sys.stdin.readline())
switches = [-1] + list(map(int, sys.stdin.readline().split()))

count_student = int(sys.stdin.readline())

for _ in range(count_student):
    sex, number = map(int, sys.stdin.readline().split())

    if sex == 1:
        for i in range(number, count + 1, number):
            switch(i)
    else:
        switch(number)

        i = min(number - 1, count - number)

        for j in range(1, i + 1):
            if switches[number + j] == switches[number - j]:
                switch(number-j)
                switch(number+j)
            else:
                break

for i in range(1, count + 1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print()
