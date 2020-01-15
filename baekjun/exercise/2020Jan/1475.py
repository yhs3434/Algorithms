# 방 번호
# https://www.acmicpc.net/problem/1475

n = input()

cHash = {'6': 0, '9': 0}

for x in n:
    if x not in cHash:
        cHash[x] = 1
    else:
        cHash[x] += 1
cHash['6'] += cHash['9']
cHash['6'] = cHash['6'] // 2 if cHash['6']//2 == cHash['6']/2 else cHash['6']//2 + 1
cHash['9'] = cHash['6']

answer = 0
for key in cHash:
    if cHash[key] > answer:
        answer = cHash[key]
print(answer)