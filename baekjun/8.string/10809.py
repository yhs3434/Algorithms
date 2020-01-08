# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

strr = input()
for i in range(26):
    aa = chr(ord('a')+i)
    if aa in strr:
        print(strr.index(aa), end=' ')
    else:
        print(-1, end= ' ')
