# 서머코딩 / 윈터코딩 (~2018)
# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    answer = 0

    cp = (0, 0)
    moved = {}
    for dir in dirs:
        if dir == 'U':
            if cp[0]+1<=5:
                ncp = (cp[0]+1, cp[1])
                flag = True
                if cp not in moved:
                    moved[cp] = [ncp]
                else:
                    if ncp not in moved[cp]:
                        moved[cp].append(ncp)
                    else:
                        flag = False
                if ncp not in moved:
                    moved[ncp] = [cp]
                else:
                    if cp not in moved[ncp]:
                        moved[ncp].append(cp)
                    else:
                        flag = False
                if flag:
                    answer += 1
        elif dir == 'R':
            if cp[1] + 1 <= 5:
                ncp = (cp[0], cp[1]+1)
                flag = True
                if cp not in moved:
                    moved[cp] = [ncp]
                else:
                    if ncp not in moved[cp]:
                        moved[cp].append(ncp)
                    else:
                        flag = False
                if ncp not in moved:
                    moved[ncp] = [cp]
                else:
                    if cp not in moved[ncp]:
                        moved[ncp].append(cp)
                    else:
                        flag = False
                if flag:
                    answer += 1
        elif dir == 'D':
            if cp[0] - 1 >= -5:
                ncp = (cp[0]-1, cp[1])
                flag = True
                if cp not in moved:
                    moved[cp] = [ncp]
                else:
                    if ncp not in moved[cp]:
                        moved[cp].append(ncp)
                    else:
                        flag = False
                if ncp not in moved:
                    moved[ncp] = [cp]
                else:
                    if cp not in moved[ncp]:
                        moved[ncp].append(cp)
                    else:
                        flag = False
                if flag:
                    answer += 1
        elif dir == 'L':
            if cp[1] - 1 >= -5:
                ncp = (cp[0], cp[1]-1)
                flag = True
                if cp not in moved:
                    moved[cp] = [ncp]
                else:
                    if ncp not in moved[cp]:
                        moved[cp].append(ncp)
                    else:
                        flag = False
                if ncp not in moved:
                    moved[ncp] = [cp]
                else:
                    if cp not in moved[ncp]:
                        moved[ncp].append(cp)
                    else:
                        flag = False
                if flag:
                    answer += 1
        cp = ncp

    return answer

print(solution(	"ULURRDLLU"))
print(solution(	"LULLLLLLU"))