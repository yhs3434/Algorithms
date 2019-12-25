# 2018 KAKAO BLIND RECRUITMENT [3차] 방금그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683

def solution(m, musicinfos):
    answer = '(None)'
    answerArr = []
    musics = {}

    idx = 0
    for info in musicinfos:
        infoArr = info.split(',')
        melodyTime = timeGap(infoArr[0], infoArr[1])
        musics[infoArr[2]] = {'time': melodyTime, 'melody': {}, 'idx': idx}
        melodies = infoArr[3]
        melodiesArr = getMelodiesArr(melodies)
        mHash = musics[infoArr[2]]['melody']
        cur = musics[infoArr[2]]['melody']
        for i in range(melodyTime):
            j = i % len(melodiesArr)
            mm = melodiesArr[j]
            if(i==0):
                mHash[mm] = {}
                cur = cur[mm]
            else:
                cur[mm] = {}
                cur = cur[mm]
        mHash = musics[infoArr[2]]['melody']
        cur = musics[infoArr[2]]['melody']
        idx += 1

    m = getMelodiesArr(m)
    maxTime = 0
    for key in musics:
        cur = musics[key]
        mTime = cur['time']
        cur = cur['melody']
        flag = False
        endFlag = False
        startC = m[0]
        while endFlag==False and flag==False:
            flag = True
            while cur!={} and startC not in cur:
                cur = cur[list(cur.keys())[0]]
            for c in m:
                if(c in cur):
                    cur = cur[c]
                else:
                    if(cur=={}):
                        flag = False
                        endFlag = True
                    else:
                        flag = False
                        break
        if flag:
            if(mTime >= maxTime):
                if(mTime > maxTime):
                    answerArr = [key]
                else:
                    answerArr.append(key)
                maxTime = mTime

    if (len(answerArr)>0):
        minIdx = float('inf')
        minKey = ''
        for key in answerArr:
            curIdx = musics[key]['idx']

            if(curIdx < minIdx):
                minIdx = curIdx
                minKey = key
        answer = minKey
    return answer

def getMelodiesArr(melodies):
    idx = 0
    length = len(melodies)
    melodiesArr = []
    while idx < length:
        m = melodies[idx]
        if (idx < length - 1):
            if (melodies[idx + 1] == '#'):
                melodiesArr.append(m + melodies[idx + 1])
                idx += 1
            else:
                melodiesArr.append(m)
        else:
            melodiesArr.append(m)
        idx += 1
    return melodiesArr

def timeGap(startT, endT):
    sh = int(startT[:2])
    sm = int(startT[3:5])
    eh = int(endT[:2])
    em = int(endT[3:5])
    return (eh - sh)*60 + (em - sm)


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(	"CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution(	"ABC", ["12:00,12:14,HELLO,C#DEC#FAAGC#AB", "13:00,13:05,WORLD,ABCDEF"]))