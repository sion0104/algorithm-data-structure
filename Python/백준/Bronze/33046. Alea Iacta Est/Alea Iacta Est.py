import sys

input = sys.stdin.readline

def find_jindong(A, B, C, D):
    current_player = 1

    first_sum = (A + B - 1) % 4
    current_player = (current_player + first_sum - 1) % 4 + 1

    second_sum = (C + D - 1) % 4
    jindong = (current_player + second_sum - 1) % 4 + 1

    return jindong

A, B = map(int, input().split())
C, D = map(int, input().split())

print(find_jindong(A, B, C, D))
