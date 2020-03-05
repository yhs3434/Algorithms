# 한다 안한다

t = int(input())
for _ in range(t):
    inp = list(map(int, list(input())))
    while len(inp)>2:
        inp = inp[1:-1]
    if inp[0] == inp[-1]:
        print('Do-it')
    else:
        print('Do-it-Not')