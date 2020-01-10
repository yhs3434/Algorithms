# 셀프 넘버
# https://www.acmicpc.net/problem/4673

def makeNextNum(n):
    nStr = str(n)
    ns = []
    for i in nStr:
        ns.append(int(i))
    return n+sum(ns)

selfNum = [i for i in range(1, 10001)]
for i in range(1, 10000):
    nn = makeNextNum(i)
    if nn in selfNum:
        selfNum.remove(makeNextNum(i))
for s in selfNum:
    print(s)