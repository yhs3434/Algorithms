def solution(s):
    answer = []

    s = s[2:-2]
    tuples = s.split('},{')
    arr = []
    for tp in tuples:
        temp = set(map(int, tp.split(',')))
        arr.append(temp)
    arr.sort(key=lambda x: len(x))
    cur = {}
    for ar in arr:
        if cur == {}:
            answer.append(list(ar)[0])
            cur = {list(ar)[0]}
        else:
            answer.append((list(ar-cur))[0])
            cur |= ar

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
