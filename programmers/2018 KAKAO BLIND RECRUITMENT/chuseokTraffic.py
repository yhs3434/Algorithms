# 2018 KAKAO BLIND [1차] 추석 트래픽
# https://programmers.co.kr/learn/courses/30/lessons/17676

def solution(lines):
    answer = 0
    heap = []
    newLines = []
    for line in lines:
        eTime = line[11:23]
        eTime = hourPlus(eTime)
        ms = line[24:-1]
        sTime = timeMinus(eTime, ms)
        newLines.append((sTime, eTime))
    newLines.sort()
    length = len(newLines)
    for i in range(length):
        endTime = getCurTime(newLines[i][1])
        count = 0
        for j in range(length):
            if(newLines[j][0]<=endTime and newLines[j][1]>=newLines[i][1]):
                count += 1
        if (count > answer):
            answer = count
    return answer

def hourPlus(time):
    h = int(time[:2])
    h += 24
    h = str(h)
    return h+time[2:]

def getCurTime(time):
    h = int(time[:2])
    m = int(time[3:5])
    s = float(time[6:])-0.001
    s += 1

    if(s>=60):
        s-=60
        m+=1
        if(m>=60):
            m-=60
            h+=1
    if (h<10):
        h = '0'+str(h)
    else:
        h = str(h)
    if (m<10):
        m = '0'+str(m)
    else:
        m = str(m)
    if (int(s)//10==0):
        s = '0'+str(s)
    else:
        s = str(s)
    return h+':'+m+':'+s

def timeMinus(time, ms):
    ms = float(ms)-0.001
    h = int(time[:2])
    m = int(time[3:5])
    s = float(time[6:])
    s -= ms
    if(s<0):
        s+=60.0
        m-=1
        if(m<0):
            m+=60
            h-=1
            if(h<0):
                h+=24
    if (h<10):
        h = '0'+str(h)
    else:
        h = str(h)
    if (m<10):
        m = '0'+str(m)
    else:
        m = str(m)
    if (int(s)//10==0):
        s = '0'+str(s)
    else:
        s = str(s)

    return h+':'+m+':'+s

print(solution([
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]))

print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(	["2016-09-15 00:00:00.000 3s"]))