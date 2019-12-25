# 2018 KAKAO BLIND RECRUITMENT [3차] 자동완성
# https://programmers.co.kr/learn/courses/30/lessons/17685

def solution(words):
    answer = 0
    myhash = {}
    for word in words:
        cur = myhash
        for w in word:
            if(w not in cur):
                cur[w] = {}
            cur = cur[w]
            if ('count' not in cur):
                cur['count'] = 1
            else:
                cur['count'] += 1

    for word in words:
        count = 0
        cur = myhash
        for i in range(len(word)):
            w = word[i]
            if(w in cur):
                cur = cur[w]
                if (cur['count'] == 1):
                    count += 1
                    break
            else:
                break
            count += 1
        answer += count

    return answer

print(solution(	["go", "gon", "gone", "guild"]))
print(solution(	["abc", "def", "ghi", "jklm"]))
print(solution(["word", "war", "warrior", "world"]))