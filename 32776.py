import sys

input = sys.stdin.readline

S_ab = int(input())
M_a, F_ab, M_b = map(int, input().split())

F_ab =  M_a + F_ab + M_b

if F_ab >= S_ab or S_ab <= 240:
    print("high speed rail")
else:
    print("flight")
