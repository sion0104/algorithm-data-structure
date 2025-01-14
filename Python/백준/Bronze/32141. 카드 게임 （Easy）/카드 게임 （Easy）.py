import sys

input = sys.stdin.readline

cards = []
cards_num, stamina = map(int, input().strip().split())
cards = list(map(int, input().split()))

result = -1
if sum(cards) < stamina:
    print(result)
else:
    for card in cards:
        result += 1
        stamina -= card

        if stamina <= 0:
            break

    print(result+1)
    