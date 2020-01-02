# 서머코딩 / 윈터코딩 (~2018) - 스티커 모으기(2)
# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    answer = 0

    if len(sticker) <= 3:
        return max(sticker)

    dp1 = [0 for i in range(len(sticker)+1)]
    dp2 = [0 for i in range(len(sticker) + 1)]
    dp3 = [0 for i in range(len(sticker) + 1)]

    dp1[1] = sticker[0]
    dp2[2] = sticker[1]
    for i in range(2, len(sticker)):
        dp1[i+1] = max(dp1[i-1] + sticker[i], dp1[i-2] + sticker[i])
        dp2[i + 1] = max(dp2[i - 1] + sticker[i], dp2[i - 2] + sticker[i])
        dp3[i + 1] = max(dp3[i - 1] + sticker[i], dp3[i - 2] + sticker[i])
    if dp1[1] != 0:
        dp1[-1] = 0
    if dp2[1] != 0:
        dp2[-1] = 0
    if dp3[1] != 0:
        dp3[-1] = 0

    answer = max([max(dp1), max(dp2), max(dp3)])

    return answer

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))