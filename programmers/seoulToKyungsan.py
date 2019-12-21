# 서울에서 경산까지
# https://programmers.co.kr/learn/courses/30/lessons/42899

def solution(K, travel):
    answer = 0

    sections = []
    for i in range(len(travel)):
        t = travel[i]
        walk = (t[0], t[1])
        ride = (t[2], t[3])
        sections.append({})
        if(i == 0):
            sections[i][walk[1]] = walk[0]
            sections[i][ride[1]] = ride[0]
        else:
            for key in sections[i-1]:
                newWalk = (sections[i-1][key]+walk[0], key+walk[1])
                newRide = (sections[i-1][key]+ride[0], key+ride[1])
                if(newWalk[0] <= K):
                    if(newWalk[1] not in sections[i]):
                        sections[i][newWalk[1]] = newWalk[0]
                    else:
                        if(newWalk[0] < sections[i][newWalk[1]]):
                            sections[i][newWalk[1]] = newWalk[0]
                if(newRide[0] <= K):
                    if (newRide[1] not in sections[i]):
                        sections[i][newRide[1]] = newRide[0]
                    else:
                        if (newRide[0] < sections[i][newRide[1]]):
                            sections[i][newRide[1]] = newRide[0]

    answer = max(sections[-1].keys())

    return answer

print(solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]))