import sys

T = int(sys.stdin.readline())

for _ in range(T):
    VPS = sys.stdin.readline()
    stack = []

    for i in VPS:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
        else:
            if not stack:
                print("YES")
            else:
                print("NO")