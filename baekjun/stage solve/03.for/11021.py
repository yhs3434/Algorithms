# A+B-7
# https://www.acmicpc.net/problem/11021

import sys

t = int(sys.stdin.readline())
for xxx in range(t):
    a, b = map(int, sys.stdin.readline().split(' '))
    print('Case #'+str(xxx+1)+':', a+b)