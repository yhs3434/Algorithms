# ROT13
# https://www.acmicpc.net/problem/11655
# https://github.com/yhs3434/Algorithms

inp = input()
answer = ''
for c in inp:
    flag = False
    if ord('A') <= ord(c) <= ord('Z'):
        flag = True
    if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
        c = c.lower()
        newC = chr((ord(c) - ord('a') + 13)%26+ord('a'))
        if flag:
            newC = newC.upper()
        answer += newC

    else:
        answer += c
print(answer)
