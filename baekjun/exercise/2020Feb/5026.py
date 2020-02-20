# 박사 과정
# https://www.acmicpc.net/problem/5026

N = int(input())
for _ in range(N):
    inp = input()
    if inp == 'P=NP':
        print('skipped')
    else:
        a, b = map(int, inp.split('+'))
        print(a+b)
