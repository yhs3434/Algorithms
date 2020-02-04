# 너의 이름은
# https://www.acmicpc.net/problem/14653
# https://github.com/yhs3434/Algorithms

n, k, q = map(int, input().split(' '))
person = {}
bef = {}
val = 0
flag = False
messages = []
chk = [False] * n
for i in range(k):
    a, b = input().split(' ')
    a = int(a)
    messages.append((a, b))

    if i >= (q-1):
        person[b] = True
        chk[ord(b)-ord('A')] = True
        if i == (q-1):
            val = a
            if a == 0:
                flag = True
    else:
        if b in bef:
            bef[b] = max(a, bef[b])
        else:
            bef[b] = a
j = 1
while (q-1-j) >= 0:
    if messages[q-1-j][0] == val:
        chk[ord(messages[q-1-j][1]) -ord('A')] = True
    else:
        break
    j += 1

if flag:
    print(-1)
else:
    for i in range(1,n):
        c = chr(ord('A') + i)
        if chk[i] == False:
            print(c, end= ' ')