# 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''

    while (n!=0):
        n -= 1
        answer = encode124(n%3) + answer
        n //= 3

    return answer

def encode124(n):
    if(n==0):
        return '1'
    elif(n==1):
        return '2'
    elif(n==2):
        return '4'
    else:
        return '0'

print(solution(10))