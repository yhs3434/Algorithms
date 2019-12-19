# 시저 암호
# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''

    ordA = ord('a')
    ordA2 = ord('A')
    for c in s:
        if(c==' '):
            answer += ' '
        else:
            ordCur = ord(c)
            if(ordCur>=97):
                ordCur -= ordA
                ordCur = (ordCur + n)%26
                ordCur += ordA
                answer += chr(ordCur)
            else:
                ordCur -= ordA2
                ordCur = (ordCur + n) % 26
                ordCur += ordA2
                answer += chr(ordCur)

    return answer

print(solution("a B z", 4))