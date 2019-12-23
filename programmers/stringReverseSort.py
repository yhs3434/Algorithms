# 문자열 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    answer = ''

    hash = {}
    for c in s:
        if c not in hash:
            hash[c] = 1
        else:
            hash[c] += 1

    keyStore = list(hash.keys())
    keyStore.sort(reverse=True)

    for key in keyStore:
        answer += (key*hash[key])

    return answer

print(solution('Zbcdefg'))