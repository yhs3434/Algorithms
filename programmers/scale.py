# 저울
# https://programmers.co.kr/learn/courses/30/lessons/42886

def solution(weight):
    answer = 0

    cur = 1
    weight.sort()
    print(weight)
    for w in weight:
        if(cur>=w):
            cur+=w
        else:
            break
    answer = cur
    return answer

print(solution([3, 1, 6, 2, 7, 30, 1]))