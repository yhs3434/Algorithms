# 입국심사
# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    length = len(times)
    right = max(times)*n
    answer = right
    left = 0
    mid = 0

    while(left<=right):
        mid = (left+right)//2
        people = 0
        for t in times:
            people += (mid//t)
        if(people < n):
            left = mid + 1
        else:
            if(mid<answer):
                answer = mid
            right = mid -1
    return answer


print(solution(6, [7, 10]))