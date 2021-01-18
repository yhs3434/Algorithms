M = int(input())
N = int(input())

avails = []
n = int(M ** (1/2)) - 1
while True:
    nn = n ** 2
    if M <= nn <= N:
        avails.append(nn)
    if nn > N:
        break
    n += 1
if avails:
    print(sum(avails))
    print(avails[0])
else:
    print(-1)