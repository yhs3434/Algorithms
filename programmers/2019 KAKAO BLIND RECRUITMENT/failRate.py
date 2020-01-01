# 2019 KAKAO BLIND RECRUITMENT 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    failRates = []
    for i in range(N):
        failRates.append(failRate(i + 1, stages))
    answer = []
    for i in range(N):
        count = 0
        maxValue = -1
        maxIndex = 0
        for rate in failRates:
            if (rate > maxValue):
                maxValue = rate
                maxIndex = count
            count += 1
        failRates[maxIndex] = -1
        answer.append(maxIndex + 1)

    return answer


def failRate(n, stages):
    numOfPlayer = 0
    numOfSuccess = 0
    failRate = 0
    for stage in stages:
        if (stage >= n):
            numOfPlayer += 1
        if (stage > n):
            numOfSuccess += 1
    if (numOfPlayer != 0):
        failRate = (numOfPlayer - numOfSuccess) / numOfPlayer
    return failRate

print(solution(	5, [2, 1, 2, 6, 2, 4, 3, 3]))