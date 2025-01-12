N = int(input())
channel = list(input() for _ in range(N))
index1, index2 = channel.index('KBS1'), channel.index('KBS2')

if index1 > index2:
    index2 += 1

print('1'*index1 + '4'*index1 + '1'*index2 + '4'*(index2-1))