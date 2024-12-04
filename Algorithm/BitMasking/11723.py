import sys

input = sys.stdin.readline

operations_num = int(input())

S = set()

for _ in range(operations_num):
    operations = list(input().split())

    if operations[0] == 'add':
        S.add(int(operations[1]))
    elif operations[0] == 'remove':
        try:
            S.remove(int(operations[1]))
        except:
            pass
    elif operations[0] == 'check':
        if int(operations[1]) in S:
            print(1)
        else:
            print(0)
    elif operations[0] == 'toggle':
        if int(operations[1]) in S:
            S.remove(int(operations[1]))
        else:
            S.add(int(operations[1]))
    elif operations[0] == 'all':
        S = set([i for i in range(1, 21)])
    else:
        S = set()
