# 5와 6의 차이
# https://www.acmicpc.net/problem/2864
# https://github.com/yhs3434

a, b = input().split(' ')
la = ''
ha = ''
lb = ''
hb = ''

for c in a:
    if c == '5' or c=='6':
        la += '5'
        ha += '6'
    else:
        la += c
        ha += c
for c in b:
    if c == '5' or c=='6':
        lb += '5'
        hb += '6'
    else:
        lb += c
        hb += c

print(int(la)+int(lb), int(ha)+int(hb))