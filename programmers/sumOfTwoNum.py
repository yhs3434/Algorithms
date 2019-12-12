# 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0

    amount = abs(b - a) + 1
    answer = (a+b)*amount//2

    return answer

def abs(n):
    if(n<0):
        return -n
    else:
        return n