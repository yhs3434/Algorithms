# 거짓말
# https://www.acmicpc.net/problem/1043
# https://github.com/yhs3434/Algorithms

N, M = map(int, input().split(' '))
K, *arr = map(int, input().split(' '))
arr = set(arr)
answer = 0

parties = []

for _ in range(M):
    x, *people = map(int, input().split(' '))
    parties.append((x, people))

eflag = True
idxs = set()
while eflag:
    eflag = False
    for i in range(len(parties)):
        if i not in idxs:
            party = parties[i]

            if len(set(party[1])&arr) > 0:
                arr = arr|set(party[1])
                eflag = True
                idxs.add(i)
print(M-len(idxs))