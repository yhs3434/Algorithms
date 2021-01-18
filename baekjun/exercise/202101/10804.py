cards = [i for i in range(1, 21)]
for i in range(10):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    temp = []
    for j in range(a, b+1):
        temp.append((a, cards[j]))
    k = 0
    while temp:
        cur = temp.pop()
        aidx = cur[0]
        card = cur[1]
        cards[aidx + k] = card
        k += 1
for c in cards:
    print(c, end=' ')