import sys
rl = sys.stdin.readline
cards = {}
avails = []
N = int(input())
for _ in range(N):
    card = int(rl().rstrip())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1
        avails.append(card)
maxCard = -float('inf')
maxVal = 0
avails.sort()
for avail in avails:
    val = cards[avail]
    if val > maxVal:
        maxVal = val
        maxCard = avail

print(maxCard)