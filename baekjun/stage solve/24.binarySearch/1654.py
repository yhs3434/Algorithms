# 랜선 자르기
# https://www.acmicpc.net/problem/1654

def solution(k, n, wires):
    left = 1
    right = max(wires)
    answer = 0
    while left<=right:
        mid = (left + right) // 2
        cnt = 0
        for wire in wires:
            cnt += (wire // mid)
        if cnt >= n:
            left = mid + 1
            if mid > answer:
                answer = mid
        else:
            right = mid - 1
    return answer

k, n = map(int, input().split(' '))
wires = []
for xxx in range(k):
    wires.append(int(input()))
print(solution(k, n, wires))