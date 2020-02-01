# 수열의 합
# https://www.acmicpc.net/problem/1024
# https://github.com/yhs3434

N, L = map(int, input().split(' '))

lenn = L
left = 0
while lenn <= 100:
    mid = 0
    if lenn % 2 == 1:
        if N % lenn == 0:
            mid = N // lenn
            left = mid - (lenn//2)

            break
        else:
            lenn += 1
            continue
    else:
        if (N + (lenn//2)) % lenn == 0:
            mid = (N+(lenn//2)) // lenn
            left = mid - (lenn//2)

            break
        else:
            lenn += 1
            continue
if left < 0 or lenn >100:
    print(-1)
else:
    for i in range(lenn):
        print(left+i, end= ' ')