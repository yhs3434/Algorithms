# 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        n1 = arr1[i]
        n2 = arr2[i]
        resultMap = ""
        for j in range(n):
            r1 = n1%2
            r2 = n2%2
            n1 //= 2
            n2 //= 2
            if(r1 == 0 and r2 == 0):
                resultMap = ' '+resultMap
            else:
                resultMap = '#' + resultMap
        answer.append(resultMap)

    return answer

print(solution(	5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))