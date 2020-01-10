# 단어 공부
# https://www.acmicpc.net/problem/1157

strr = input().upper()
hmap = {}
for c in strr:
    if c not in hmap:
        hmap[c] = 1
    else:
        hmap[c] += 1
maxCnt = 0
maxChar = []
for key in hmap:
    if hmap[key] > maxCnt:
        maxChar = [key]
        maxCnt = hmap[key]
    elif hmap[key] == maxCnt:
        maxChar.append(key)

if len(maxChar)>1:
    print('?')
else:
    print(maxChar[0])