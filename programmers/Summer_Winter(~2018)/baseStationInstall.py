# 서머코딩 / 윈터코딩 (~2018) - 기지국 설치
# https://programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    answer = 0

    left = 1
    right = 0

    for station in stations:
        right = station - w - 1
        amount = 0
        if left <= right:
            amount = getAmount(left, right)
        answer += getNeed(amount, 2*w+1)
        left = station + w + 1
    right = n
    amount = 0
    if left <= right:
        amount = getAmount(left, right)
    answer += getNeed(amount, 2*w+1)

    return answer

def getAmount(left, right):
    return right - left + 1

def getNeed(amount, w):
    if amount <= 0: return 0
    return (amount - 1) // w + 1

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))