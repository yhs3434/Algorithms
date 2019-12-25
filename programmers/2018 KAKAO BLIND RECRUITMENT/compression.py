# 2018 KAKAO BLIND RECRUITMENT [3차] 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3

def solution(msg):
    answer = []

    ordA = ord('A')
    dictionary = {}
    for i in range(26):
        dictionary[chr(ordA + i)] = {'val' :i+1}
    idx = 27
    length = len(msg)
    j = 0
    for i in range(length):
        if (j>=length):
            break
        c = msg[j]
        cur = dictionary
        while c in cur:
            cur = cur[c]
            j += 1
            if(j<length):
                c = msg[j]
            else:
                break
        val = cur['val']
        cur[c] = {'val': idx}
        idx += 1

        answer.append(val)
    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))