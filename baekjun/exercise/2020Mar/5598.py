# 카이사르 암호
# https://www.acmicpc.net/problem/5598
# https://github.com/yhs3434/Algorithms

inp = input()
ans = ''
for c in inp:
    ordd = ord(c) - 3 - ord('A')
    if ordd<0:
        ordd += 26
    ans += chr(ordd + ord('A'))
print(ans)