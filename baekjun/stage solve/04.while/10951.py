# https://www.acmicpc.net/problem/10951

import sys

while True:
    lists = sys.stdin.readline().rstrip()
    if len(lists)!=3:
        break
    a, b = map(int, lists.split(' '))
    print(a+b)