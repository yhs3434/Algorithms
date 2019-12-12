# 가운데 글자 가져오기
# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    mid = 0
    length = len(s)

    if(length %2 == 0):
        mid = length//2-1
        answer = s[mid:mid+2]
    else:
        mid = length//2
        answer = s[mid]


    return answer

print(solution('abc'))