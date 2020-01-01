# 연습문제 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ''

    ss = s.split(' ')
    for word in ss:
        for i in range(len(word)):
            c = word[i]
            if i%2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
    answer = answer[:-1]
    return answer

print(solution('try hello world'))