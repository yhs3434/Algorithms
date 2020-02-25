import sys
rl = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, m = map(int, rl().rstrip().split(' '))
    inp = list(rl().rstrip())
    p = list(map(int, rl().rstrip().split(' ')))
    p.sort()

    answer = [0]*26
    keyboards = []
    bef = 0
    for pp in p:
        keyboard = [0]*26
        for i in range(bef, pp):
            keyboard[ord(inp[i])-ord('a')] += 1
        bef = pp
        keyboards.append(keyboard)
    lenn = len(keyboards)
    kidx = 0
    while lenn > 0:
        curKeyboard = keyboards[kidx]
        for i in range(len(answer)):
            answer[i] += curKeyboard[i]*lenn
        lenn -= 1
        kidx += 1
    for inpp in inp:
        answer[ord(inpp) - ord('a')] += 1
    for a in answer:
        print(a, end=' ')
    print('')