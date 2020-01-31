# 문자열 화폐
# https://www.acmicpc.net/problem/17828
# https://github.com/yhs3434/Algorithms

n, x = map(int, input().split(' '))
if 26*n < x or n > x:
    print('!')
else:
    answer = ''

    delim = 26
    while n > 0 and delim > 0:
        clen = x // delim   # 2
        while (n-clen)*(delim) < (x-clen*delim) or (n-clen) > (x-clen*delim):
            clen -= 1
            if clen == 0:
                break
        if clen==0:
            delim -= 1
            continue
        else:
            x -= clen*delim
            n -= clen
            answer = chr(ord('A') + delim - 1)*(clen) + answer
            delim -= 1


    print(answer)