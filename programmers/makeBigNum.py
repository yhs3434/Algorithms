# 큰 수 만들기
# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    length = len(number)
    m = 0
    beforeLen = length
    for i in range(k):
        flag = False
        for i in range(m, length-1):
            if(number[i]<number[i+1]):
                number = number[:i]+number[i+1:]
                if(i>0):
                    m = i-1
                length -= 1
                flag = True
                break
            else:
                continue
        if (flag==False):
            number = number[:-1]
            length -= 1
    return number

print(solution("1111", 2))