# 문자열 내 마음대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []

    strings.sort()
    strings.sort(key=lambda key: key[n])
    answer = strings
    return answer

print(solution(	["sun", "bed", "car"], 1))
print(solution(	["abce", "abcd", "cdx"], 2))