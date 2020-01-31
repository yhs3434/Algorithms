# 카드게임
# https://www.acmicpc.net/problem/10801
# https://github.com/yhs3434/Algorithms

a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

cnt = [0, 0]

for i in range(len(a)):
    if a[i] > b[i]:
        cnt[0] += 1
    elif a[i] < b[i]:
        cnt[1] += 1

if cnt[0] > cnt[1]:
    print('A')
elif cnt[0] < cnt[1]:
    print('B')
else:
    print('D')