# 이상한 나라의 암호
# https://www.acmicpc.net/problem/18245
# https://github.com/yhs3434/Algorithms

i = 0
while True:
    inp = input()
    i += 1
    if inp == 'Was it a cat I saw?':
        break

    delim = 0
    while delim < len(inp):
        print(inp[delim], end='')
        delim += 1
        delim += i
    print('')