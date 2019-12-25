# 2018 KAKAO BLIND RECRUITMENT [1차] 셔틀버스
# https://programmers.co.kr/learn/courses/30/lessons/17678

import queue

def solution(n, t, m, timetable):
    answer = ''

    q = queue.Queue()

    timetable.sort(reverse=True)
    curTime = "09:00"
    lastPerson = ''
    while n>0:
        while timetable and timetable[-1]<=curTime:
            q.put(timetable.pop())
        count = m
        while count>0 and q.empty()==False:
            person = q.get()
            if(person>curTime):
                q.put(person)
                break
            else:
                lastPerson = person
            count -= 1
        n -= 1
        if(n==0):
            if(count > 0):
                answer = curTime
            else:
                answer = timeMinus(lastPerson, 1)
        curTime = timePlus(curTime, t)

    return answer

def timePlus(time, minute):
    h = int(time[:2])
    m = int(time[3:])
    m += minute
    if(m>=60):
        m-=60
        h+=1
    if(m<10):
        m = '0'+str(m)
    else:
        m = str(m)
    if(h<10):
        h = '0'+str(h)
    else:
        h = str(h)
    return h+":"+m

def timeMinus(time, minute):
    h = int(time[:2])
    m = int(time[3:])
    m -= minute
    if(m<0):
        m+=60
        h-=1
    if (m < 10):
        m = '0' + str(m)
    else:
        m = str(m)
    if (h < 10):
        h = '0' + str(h)
    else:
        h = str(h)
    return h+":"+m

print(solution(1,1,5, ['08:00', '08:01', '08:02', '08:03']))