# 2020 KAKAO BLIND RECRUITMENT 기둥과 보 설치
# https://programmers.co.kr/learn/courses/30/lessons/60061

# [x, y, a, b]
# x, y : 좌표, a : (0: 기둥, 1: 보), b: (0: 삭제, 1: 설치)

def solution(n, build_frame):
    builded = []
    for bf in build_frame:
        if bf[3] == 1:  # 설치
            if isAvail(bf, builded):
                builded.append([bf[0], bf[1], bf[2]])
        elif bf[3] == 0:    # 삭제
            builded.remove([bf[0], bf[1], bf[2]])
            flag = False
            for bd in builded:
                if not isAvail(bd, builded):
                    flag = True
                    break
            if flag:
                builded.append([bf[0], bf[1], bf[2]])

    builded.sort(key = lambda key: key[2])
    builded.sort(key=lambda key: key[1])
    builded.sort(key=lambda key: key[0])

    return builded

def isAvail(bf, builded):
    # x, y : 좌표, a : (0: 기둥, 1: 보), b: (0: 삭제, 1: 설치)

    x = bf[0]
    y = bf[1]
    a = bf[2]

    if a == 0:
        if y == 0 or [x-1, y, 1] in builded or [x, y, 1] in builded or [x, y-1, 0] in builded:
            return True
    elif a == 1:
        if [x, y-1, 0] in builded or [x+1, y-1, 0] in builded or ([x-1, y, 1] in builded and [x+1, y, 1] in builded):
            return True
    return False


print(solution(	5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(	5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))