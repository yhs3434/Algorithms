# Count Me In
# https://www.acmicpc.net/problem/11319
# https://github.com/yhs3434/Algorithms

vowels = ['A','E','I','O','U','a','e','i','o','u']

s = int(input())
for xxx in range(s):
    inp = input()
    cc = 0
    vc = 0
    for c in inp:
        if c == ' ':
            continue
        elif c in vowels:
            vc += 1
        else:
            cc += 1
    print(cc, vc)