# 일반 화학 실험
# https://www.acmicpc.net/problem/4766
# https://github.com/yhs3434

bef = -11
while True:
    num = float(input())
    if num==999:
        break
    if bef == -11:
        bef = num
    else:
        print('%.2f'%(num - bef))
        bef = num