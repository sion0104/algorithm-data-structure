import sys

input = sys.stdin.readline

S = input().rstrip()

if len(S) <= 2 or not (S[0] == "\"" and S[-1] == "\""):
    print("CE")
else:
    print(S[1:-1])
