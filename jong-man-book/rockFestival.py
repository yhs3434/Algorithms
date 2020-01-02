# 록 페스티벌 (난이도: 하)

C = int(input())
answer = []
for i in range(C):
    N, L = map(int, input().split(' '))
    costs = list(map(int, input().split(' ')))

    averages = []
    for i in range(L, N+1):
        for j in range(N-i+1):
            costs[j: j+i]
            averages.append(sum(costs[j: j+i])/i)
    answer.append(min(averages))

for a in answer:
    print(a)