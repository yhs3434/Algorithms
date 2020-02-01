# 파티가 끝나고 난 뒤
# https://www.acmicpc.net/problem/2845
# https://github.com/yhs3434/Algorithms

l, p = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

val = l*p
for a in arr:
    print(a-val, end=' ')