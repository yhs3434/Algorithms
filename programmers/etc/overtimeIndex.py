# 연습문제 - 야근 지수
# https://programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    answer = 0

    visit = {}
    for work in works:
        if work not in visit:
            visit[work] = 1
        else:
            visit[work] += 1

    maxKey = max(visit.keys())

    while n > 0:
        maxKey = max(visit.keys())
        amt = visit[maxKey]
        n -= amt
        if (maxKey-1) not in visit:
            visit[maxKey-1] = amt
        else:
            visit[maxKey-1] += amt
        del visit[maxKey]
    if n != 0:
        visit[maxKey] = -n
        visit[maxKey-1] += n

    for key in visit:
        if key > 0:
            answer += (key ** 2) * visit[key]

    return answer

print(solution(4, [4,3,3]))
print(solution(3, [1,1]))