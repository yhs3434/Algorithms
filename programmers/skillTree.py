# 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0
    length = len(skill_trees)
    for i in range(length):
        st = skill_trees[i]
        newSt = ''
        for s in st:
            if(s in skill):
                newSt += s
        skill_trees[i] = newSt

    for st in skill_trees:
        flag = True
        idx = 0
        for s in st:
            if(s == skill[idx]):
                idx += 1
            else:
                flag = False
        if (flag == True):
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]	))