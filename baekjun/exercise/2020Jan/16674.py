# 2018년을 되돌아보며
# https://www.acmicpc.net/problem/16674
# https://github.com/yhs3434

stan = ['1', '2', '0', '8']

inp = input()
flag = True
chash = {
    '1' : 0,
    '2' : 0,
    '0' : 0,
    '8' : 0
}
for c in inp:
    if c not in stan:
        flag = False
        break
    else:
        chash[c] += 1

if not flag:
    print(0)
else:
    flag = True
    same = True
    before = chash['0']
    for key in chash:
        if chash[key] == 0:
            flag = False
        if chash[key] != before:
            same = False
    if not flag:
        print(1)
    else:
        if same:
            print(8)
        else:
            print(2)
