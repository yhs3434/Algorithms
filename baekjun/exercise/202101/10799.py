inp = input()
cnt = 0
answer = 0

bef = ''
for ch in inp:
    if ch == '(':
        cnt += 1
    else:
        cnt -= 1
        if bef == '(':
            answer += cnt
        elif bef == ')':
            answer += 1
    bef = ch
print(answer)