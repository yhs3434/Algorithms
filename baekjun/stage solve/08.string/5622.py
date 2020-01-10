# 다이얼
# https://www.acmicpc.net/problem/5622

def getNum(c):
    if c=='A' or c=='B' or c=='C':
        return 2+1
    elif c=='D' or c=='E' or c=='F':
        return 3+1
    elif c=='G' or c=='H' or c=='I':
        return 4+1
    elif c=='J' or c=='K' or c=='L':
        return 5+1
    elif c=='M' or c=='N' or c=='O':
        return 6+1
    elif c=='P' or c=='Q' or c=='R' or c=='S':
        return 7+1
    elif c=='T' or c=='U' or c=='V':
        return 8+1
    elif c=='X' or c=='Y' or c=='Z' or c=='W':
        return 9+1
    else:
        return 10+1

s = input()
sumVal = 0
for c in s:
    sumVal += getNum(c)
print(sumVal)