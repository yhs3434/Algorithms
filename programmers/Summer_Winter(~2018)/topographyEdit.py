# 서머코딩 / 윈터코딩 (~2018) - 지형 편집
# https://programmers.co.kr/learn/courses/30/lessons/12984

def solution(land, P, Q):
    answer = float('inf')

    newLand = []
    for l in land:
        newLand += l
    n = len(newLand)
    newLand.sort()
    totalLand = [0 for i in range(n)]
    curSum = 0
    for i in range(n):
        curSum += newLand[i]
        totalLand[i] = curSum
    #print(newLand, totalLand)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        h = newLand[mid]

        pAmount = (mid * h) - (totalLand[mid]-h)
        qAmount = totalLand[-1] - (h * (n-mid)) - (totalLand[mid]-h)
        val = pAmount*P + qAmount*Q

        mid2 = mid + 1
        val2 = val
        while mid2 < n and newLand[mid] == newLand[mid2]:
            mid2 += 1
        if mid2 == n:
            val2 = val
        else:
            h = newLand[mid2]
            pAmount = (mid2 * h) - (totalLand[mid2] - h)
            qAmount = totalLand[-1] - (h * (n - mid2)) - (totalLand[mid2] - h)
            val2 = pAmount*P + qAmount*Q
        #print(mid,val, mid2, val2)
        if val <= val2:
            right = mid - 1
            if val < answer:
                answer = val
        elif val2 < val:
            left = mid + 1
            if val2 < answer:
                answer = val2

    return answer

print(solution([[4, 4, 3], [3, 2, 2], [ 2, 1, 0 ]]	, 5, 3))