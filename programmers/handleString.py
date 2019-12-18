# 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = True

    length = len(s)
    if(length!=4 and length!=6):
        answer = False
    else:
        for c in s:
            if(c>='0' and c<='9'):
                continue
            else:
                answer = False

    return answer