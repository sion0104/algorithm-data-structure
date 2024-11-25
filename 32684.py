import sys

input = sys.stdin.readline

scores= [13, 7, 5, 3, 3, 2]

cho = map(int, input().split())
han = map(int, input().split())

cho_score = sum(c * s for c, s in zip(cho, scores))
han_score = sum(h * s for h, s in zip(han, scores)) + 1.5

print('cocjr0208' if cho_score > han_score else 'ekwoo')
