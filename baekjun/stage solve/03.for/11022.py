# A+B - 8
#   https://www.acmicpc.net/problem/11022

import sys

t = int(sys.stdin.readline())
for xxx in range(t):
    a, b = map(int, sys.stdin.readline().split(' '))
    print('Case #'+str(xxx+1)+':',a,'+',b,'=', a+b)