# 서머코딩 / 윈터코딩 (~2018) 쿠키 구입
# https://programmers.co.kr/learn/courses/30/lessons/49995

def solution(cookie):
    answer = 0

    for i in range(1, len(cookie)):
        leftCookie = cookie[:i]
        rightCookie = cookie[i:]
        leftSum = sum(leftCookie)
        rightSum = sum(rightCookie)
        li = 0
        ri = len(rightCookie) - 1
        while leftSum != rightSum:
            if leftSum > rightSum:
                leftSum -= leftCookie[li]
                li += 1
                if li >= len(leftCookie):
                    break
            elif leftSum < rightSum:
                rightSum -= rightCookie[ri]
                ri -= 1
                if ri < 0:
                    break
        if leftSum == rightSum:
            if leftSum > answer:
                answer = leftSum

    return answer

print(solution([1,1,2,3]))
print(solution([1,1,2,3,5,7,7,87]))
print(solution([1,2,4,5]))