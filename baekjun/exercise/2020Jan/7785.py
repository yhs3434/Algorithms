# 회사에 있는 사람
# https://www.acmicpc.net/problem/7785

n = int(input())
phash = {}
for i in range(n):
    p, el = input().split(' ')
    if el == 'enter':
        phash[p] = True
    else:
        del phash[p]
people = list(phash.keys())
people.sort(reverse=True)
for p in people:
    print(p)