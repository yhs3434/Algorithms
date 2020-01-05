# https://www.acmicpc.net/problem/10952

import sys

a, b = map(int, sys.stdin.readline().split(' '))
while a!=0 or b!=0:
    print(a+b)
    a, b = map(int, sys.stdin.readline().split(' '))