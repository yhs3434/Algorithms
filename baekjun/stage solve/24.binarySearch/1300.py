# K번째 수
# https://www.acmicpc.net/problem/1300
# https://github.com/yhs3434

def volLow(n, mid):
    sumVal = 0
    for i in range(1, n+1):
        sumVal += min(n, (mid//i))
    return sumVal

n = int(input())
k = int(input())

if n == 1:
    print(1)
else:
    left = 1
    right = n*n
    answer = float('inf')
    while left <= right:
        mid = (left + right) // 2
        vol = volLow(n, mid)
        if vol < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    print(answer)