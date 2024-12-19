import sys
import math

input = sys.stdin.readline

rows, columns, n_rows, m_columns = map(int, input().split())

row = math.ceil(rows/(n_rows+1))
column = math.ceil(columns/(m_columns+1))

print(row * column)
