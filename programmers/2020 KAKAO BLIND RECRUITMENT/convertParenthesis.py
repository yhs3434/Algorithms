# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''

    answer = makeRight(p)

    return answer

def makeRight(p):
    answer = ''
    if(p==''):
        return ''
    u, v = stepTwo(p)
    if (isRight(u)):
        answer += u
        answer += makeRight(v)
    else:
        answer += '('
        answer += makeRight(v)
        answer += ')'
        newU = u[1:-1]
        for i in range(len(newU)):
            if(newU[i] == '('):
                newU = newU[:i]+ ')' +newU[i+1:]
            else:
                newU = newU[:i] + '(' + newU[i + 1:]
        answer += newU
    return answer

def stepTwo(p):
    sCount = 0
    idx = 0
    for i in range(len(p)):
        idx = i
        x = p[i]
        if(x=='('):
            sCount -= 1
        else:
            sCount += 1
        if(sCount == 0):
            break
    u = p[:idx+1]
    v = p[idx+1:]
    return u, v

def isRight(p):
    flag = True
    sCount = 0
    for x in p:
        if(x=='('):
            sCount -= 1
        else:
            sCount += 1
        if(sCount > 0):
            flag = False
            break
    return flag

print(solution("()))((()"))