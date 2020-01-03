# 연습문제 - 가장 긴 팰린드롬
# https://programmers.co.kr/learn/courses/30/lessons/12904

import queue

def solution(s):
    answer = 0

    left = 1
    right = len(s)

    while left <= right:
        mid = (left + right) // 2
        flag1 = False
        mid2 = 0
        for ii in range(len(s)-mid+1):
            flag3 = False

            flag2 = True
            i = ii
            j = i + mid - 1
            while i<=j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    flag2 = False
                    break
            if flag2:
                flag3 = True
                if mid >= mid2:
                    mid2 = mid

            flag2 = True
            i = ii
            j = ii + mid - 2
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    flag2 = False
                    break
            if flag2:
                flag3 = True
                if mid-1 >= mid2:
                    mid2 = mid-1

            flag2 = True
            j = ii + mid - 1
            i = ii + 1
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    flag2 = False
                    break
            if flag2:
                flag3 = True
                if mid-1 >= mid2:
                    mid2 = mid-1

            if flag3:
                flag1 = True
                break

        if flag1:
            left = mid + 1
            if mid2 > answer:
                answer = mid2
        else:
            right = mid - 1

    return answer

print(solution('$#a#b#c#d#e#f#e#@'))
print(solution('abcdcbawefwefwefa'))
print(solution('abacde'))
print(solution('affjiawejfiwelfjifwefiwefijweilfweifjeewwaeeabcwefjewhfiwedesedcbafafwbb'))