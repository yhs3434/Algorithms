N = int(input())

answer = ''
if N == 0:
    answer ='0'
delim = -2

while N != 0:
    if (N % (-2) == 0):
        answer = '0' + answer
        N //= -2
    else:
        answer = '1' + answer
        N = (N - 1) // -2

print(answer)