# 2018 KAKAO BLIND RECRUITMENT [1차] 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0

    newDarts = []
    for i in range(len(dartResult)):
        d = dartResult[i]
        if(d=='S' or d=='D' or d=='T'):
            if(i==(len(dartResult)-1)):
                if(dartResult[i-2]=='1'):
                    newDarts.append(dartResult[i-2] + dartResult[i - 1] + d)
                else:
                    newDarts.append(dartResult[i-1]+d)
            else:
                if(dartResult[i+1]=='*' or dartResult[i+1]=='#'):
                    if (dartResult[i - 2] == '1'):
                        newDarts.append(dartResult[i - 2] + dartResult[i - 1] + d + dartResult[i+1])
                    else:
                        newDarts.append(dartResult[i-1]+d+dartResult[i+1])
                else:
                    if (dartResult[i - 2] == '1'):
                        newDarts.append(dartResult[i - 2] + dartResult[i - 1] + d)
                    else:
                        newDarts.append(dartResult[i - 1] + d)

    scores = [0 for i in range(len(newDarts))]

    for i in range(len(newDarts)):
        dart = newDarts[i]
        scores[i] = getScore(dart)
        if(dart[-1] == '*' or dart[-1] == '#'):
            if(dart[2] == '*'):
                if(i>0):
                    scores[i-1] *= 2
                scores[i] *= 2
            else:
                scores[i] = -scores[i]

    answer = sum(scores)
    return answer

def getScore(dart):
    score = 0
    if(dart[1]=='S' or dart[1]=='D' or dart[1]=='T'):
        score = int(dart[0])
        if(dart[1] == 'D'):
            score = score ** 2
        elif(dart[1] == 'T'):
            score = score ** 3
    else:
        score = int(dart[:2])
        if (dart[2] == 'D'):
            score = score ** 2
        elif (dart[2] == 'T'):
            score = score ** 3
    return score

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))