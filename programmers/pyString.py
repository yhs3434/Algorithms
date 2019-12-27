def solution(s):
    answer = True
    s = s.lower()
    pc = s.count('p')
    yc = s.count('y')
    print(pc, yc)
    if(pc == yc):
        return True
    else:
        return False
    return True

print(solution("pPoooyY	"))
print(solution("Pyy"))