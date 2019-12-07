def solution(participant, completion):
    answer = ''

    map = {}
    for p in participant:
        if p not in map:
            map[p] = 1
        else:
            map[p] += 1

    for c in completion:
        map[c] -= 1

    for key in map:
        if(map[key]!=0):
            answer = key
            break

    return answer

solution(['mislav', 'stanko', 'mislav', 'ana','mislav'], ['stanko', 'ana', 'mislav'])