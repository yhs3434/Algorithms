# 쌍둥이 역설
# https://www.acmicpc.net/problem/4706
# https://github.com/yhs3434

while True:
    a, b = map(float, input().split(' '))
    if a==0 and b==0:
        break
    c = 299792458
    y = b/a
    v = (-(c**2)*(y**2 - 1))**0.5
    print('%.3f'%(v/c))