import sys
rl = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(rl().rstrip())
    S = []
    answer = ''
    for __ in range(N):
        S.append(rl().rstrip())
    avails = []
    avail = [0] * N
    while True:
        flag = True
        newS = []
        for i in range(N-1):
            str0 = ''
            if avail[i] == 0:
                str0 = S[i]
            else:
                str0 = S[i][::-1]
            str1 = ''
            if avail[i+1] == 0:
                str1 = S[i+1]
            else:
                str1 = S[i+1][::-1]
            if str0 > str1:
                flag=False
                break
        if flag:
            answer = avail
            break
        avail[-1] = avail[-1] + 1
        for i in range(N-1, -1, -1):
            if avail[i] == 2:
                avail[i-1] = avail[i-1] + 1
                avail[i] = 0
    for a in answer:
        print(a, end='')
    print()