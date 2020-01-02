# 연습문제 - JadenCase 문자열 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''

    words = s.split(' ')
    print(words)
    for word in words:
        if len(word) == word.count(' '):
            flag = True
        elif len(word) > 1:
            word = word[0].upper() + word[1:].lower()
        else:
            word = word[0].upper()
        answer += (word + ' ')

    answer = answer[:-1]

    return answer

print(solution('3people  good   h i gg 23do2 '))