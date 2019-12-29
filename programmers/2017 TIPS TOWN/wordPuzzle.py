# 2017 팁스타운 단어퍼즐
# https://programmers.co.kr/learn/courses/30/lessons/12983

import queue

def solution(strs, t):
    answer = 0

    dp = [0 for i in range(len(t) + 1)]
    for i in range(1, len(t)+1):
        cnts = []
        m = 0
        if(i > 5):
            m = i - 5
        for j in range(m, i):
            cnt = 0
            if t[j:i] in strs:
                cnt = dp[j] + 1
            else:
                cnt = float('inf')
            cnts.append(cnt)
        dp[i] = min(cnts)
    answer = dp[-1] if dp[-1] != float('inf') else -1

    return answer

print(solution(	["ab", "na", "n", "a", "bn"], "nabnabn"))
print(solution(	["ba", "na", "n", "a"], "banana"))
print(solution(	["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))
print(solution(	["ba", "an", "nan", "ban", "n"], "banana"))
print(solution(['bb', 'b'], 'bbbbbb'))