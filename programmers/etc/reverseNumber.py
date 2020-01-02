# 자연수 뒤집어 배열로 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    temp = []
    lenN = len(str(n)) - 1
    while lenN >= 0:
        temp.append(n//(10**lenN))
        n %= (10**lenN)
        lenN -= 1
    answer = []
    for t in temp:
        answer = [t] + answer
    return answer

print(solution(12345))
print(solution(987654321123445))