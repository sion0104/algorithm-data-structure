import sys

while True:
    line = sys.stdin.readline()
    stack = []

    if line[0] == '.':
        break
    else:
        line.rstrip()
        for char in line:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    print('no')
                    break
                else:
                    stack.pop()
            elif char == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    print('no')
                    break
                else:
                    stack.pop()
            elif char == '.':
                if len(stack) == 0:
                    print('yes')
                else:
                    print('no')


