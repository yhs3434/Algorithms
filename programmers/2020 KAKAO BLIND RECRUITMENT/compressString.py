# 2020 KAKAO BLIND RECRUITMENT 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = float('inf')
    if len(s)==1:
        return 1

    sLen = len(s)
    for curLen in range(1, sLen//2+1):
        newStr = ''
        before = ''
        cnt = 0
        idx = 0
        for i in range(0, sLen-curLen+1, curLen):
            curWin = s[i:i+curLen]
            if i == 0:
                cnt = 1
            else:
                if(curWin == before):
                    cnt += 1
                else:
                    if cnt == 1:
                        newStr += before
                    else:
                        newStr += (str(cnt)+before)
                        cnt = 1
            before = curWin
            idx = i
        if cnt == 1:
            newStr += s[idx:]
        else:
            newStr += (str(cnt) + before + s[idx+curLen:])
        nLen = len(newStr)
        if nLen < answer:
            answer = nLen

    return answer

def solution2(s):
    answer = float('inf')

    sLen = len(s)
    for curLen in range(1, sLen//2+1):
        newStr = ''
        i = 0
        while i<(sLen-curLen+1):
            sWin = s[i : i+curLen]
            cnt = 1
            before = sWin
            j = i+curLen
            while True:
                curWin = s[j: j + curLen]
                if curWin == before:
                    j = j + curLen
                    cnt += 1
                else:
                    break
            if cnt == 1:
                if (i == 0):
                    break
                newStr += s[i]
                i += 1
            else:
                newStr += (str(cnt) + sWin)
                i = j
        newStr += s[i:]
        nLen = len(newStr)
        if nLen < answer:
            answer = nLen

    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xaxaxaxaxaxaxaxaxaxaxaxaxaxaxaxaxaxababcdcdababcdcd"))
print(solution('xx'))