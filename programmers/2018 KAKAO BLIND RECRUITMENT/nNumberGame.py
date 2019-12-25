# 2018 KAKAO BLIND RECRUITMENT [3차] n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    games = []
    i =- 1
    while len(games)<(t+1)*m:
        i += 1
        curNum = getNNumber(n, i)
        games.extend(curNum)

    for i in range(t):
        j = m*i + (p-1)
        answer += games[j]

    return answer

def getNNumber(n, num):
    resultNum = ''
    if num==0:
        return '0'
    while num>0:
        temp = 0
        temp = str(num % n)
        if temp=='10':
            temp = 'A'
        elif temp=='11':
            temp = 'B'
        elif temp=='12':
            temp = 'C'
        elif temp=='13':
            temp = 'D'
        elif temp=='14':
            temp = 'E'
        elif temp=='15':
            temp = 'F'
        resultNum = temp + resultNum
        num //= n
    return resultNum

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))