# 연습문제 - 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''

    for i in range(len(phone_number)-4):
        answer += '*'
    answer += phone_number[-4:]

    return answer

print(solution('01033334444'))