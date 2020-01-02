# 연습문제 - 최솟값 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    while A:
        answer += (A.pop() * B.pop())
    return answer

print(solution([1,4,2], [5,4,4]))