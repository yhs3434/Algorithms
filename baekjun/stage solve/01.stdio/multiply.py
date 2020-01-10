# 곱셈
# https://www.acmicpc.net/problem/2588

n1 = int(input())
n2 = int(input())

vals = []
while n2 > 0:
    vals.append(n1*(n2%10))
    n2 //= 10

answer = 0
delim = 0
while delim<3:
    answer += vals[delim]*(10**delim)
    delim += 1
for v in vals:
    print(v)
print(answer)
