# 모음의 개수
# https://www.acmicpc.net/problem/1264

def isVowel(c):
    if c == 'a':
        return True
    elif c == 'e':
        return True
    elif c == 'i':
        return True
    elif c == 'o':
        return True
    elif c == 'u':
        return True
    else:
        return False

while True:
    strr = input()
    if strr == '#':
        break
    strr = strr.lower()
    cnt = 0
    for c in strr:
        if isVowel(c):
            cnt += 1
    print(cnt)