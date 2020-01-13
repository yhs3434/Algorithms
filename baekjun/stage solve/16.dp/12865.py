# 평범한 배낭
# https://www.acmicpc.net/problem/12865

import sys
rl = sys.stdin.readline

def solution(n, k, things):
    things.sort()
    avails = [(k, 0)]   # (남은 무게, 가치)
    answer = []

    for thing in things:
        aLen = len(avails)
        for j in range(aLen):
            j = aLen - j - 1
            avail = avails[j]
            if thing[0] <= avail[0]:
                avails.append((avail[0]-thing[0], avail[1]+thing[1]))
            else:
                answer.append(avail)
                del avails[j]
    answer.extend(avails)
    answer.sort(key=lambda key: key[1])
    return answer[-1][1]


things = []
n, k = map(int, rl().rstrip().split(' '))
for xxx in range(n):
    thing = rl().rstrip().split(' ')
    things.append(tuple(map(int, thing)))
print(solution(n, k, things))