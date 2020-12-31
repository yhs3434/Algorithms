inp = input()
N = int(input())
words = set()
for _ in range(N):
    words.add(input())

flag = False
for i in range(26):
    x = chr(ord('a')+i)
    newInp = ''
    for j in range(len(inp)):
        c = inp[j]
        if ord('a') <= ord(c) <= ord('z'):
            newInp += chr((ord(c) + i - ord('a')) % 26 + ord('a'))
        elif ord('A') <= ord(c) <= ord('Z'):
            newInp += chr((ord(c) + i - ord('A')) % 26 + ord('A'))
    for word in words:
        if word in newInp:
            print(newInp)
            flag = True
            break
    if flag:
        break