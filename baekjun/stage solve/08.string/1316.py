# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

def isGroup(word):
    befores = []
    before = ''
    for c in word:
        if c != before:
            if c in befores:
                return False
            else:
                befores.append(c)
        before = c
    return True

N = int(input())
answer = 0
for xxx in range(N):
    word = input()
    if isGroup(word):
        answer += 1
print(answer)