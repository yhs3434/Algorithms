# 평범한 배낭
# https://www.acmicpc.net/problem/12865

def solution(k, things):
    things.sort()
    dp = [0 for i in range(k+1)]
    for i in range(len(things)):
        thing = things[i]
        for j in range(k, thing[0]-1, -1):
            dp[j] = max(thing[1] + dp[j-thing[0]], dp[j])
    return dp[-1]

n, k = map(int, input().split(' '))
things = []
for xxx in range(n):
    things.append(tuple(map(int, input().split(' '))))
print(solution(k, things))