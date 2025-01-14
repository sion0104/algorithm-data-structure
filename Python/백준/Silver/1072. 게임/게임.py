import decimal
import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

# Z = int((Y / X) * 100)
Z = (Y*100) // X

if Z < 99:
    result = 0
    left, right = 1, X

    while left <= right:
        mid = (left + right) // 2
        if int(((Y + mid) / (X + mid)) * 100) > Z:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(result)
else:
    print(-1)

# 파이썬 부동소수점 오차
# 실수형 계산 시 주의
# decimal.Decimal, math.fsum(), round(), float.as_integer_ratio(), math.is_clost()
