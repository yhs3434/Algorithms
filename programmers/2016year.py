# 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''

    count = 0
    for i in range(1, a):
        count += getMonth(i)
    count += (b-1)

    answer = getDay((count+5)%7)

    return answer

def getMonth(n):
    if (n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12):
        return 31
    else:
        if(n == 2):
            return 29
        else:
            return 30

def getDay(n):
    if (n == 0):
        return 'SUN'
    elif (n == 1):
        return 'MON'
    elif (n == 2):
        return 'TUE'
    elif (n == 3):
        return 'WED'
    elif (n == 4):
        return 'THU'
    elif (n == 5):
        return 'FRI'
    elif (n == 6):
        return 'SAT'
    elif (n == 7):
        return None

print(solution(5, 24))