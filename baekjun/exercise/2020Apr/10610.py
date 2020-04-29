N = list(map(int, list(input())))
answer = ''

if 0 not in N:
    print('-1')
else:
    if sum(N) %3 != 0:
        print('-1')
    else:
        N.sort()
        while N:
            answer += str(N.pop())
        print(answer)