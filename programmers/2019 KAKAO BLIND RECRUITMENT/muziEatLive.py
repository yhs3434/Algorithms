# 2019 KAKAO BLIND RECRUITMENT 무지의 먹방 라이브
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):
    answer = 0
    if(sum(food_times) <= k):
        return -1
    length = len(food_times)
    left = 0
    right = max(food_times)
    maxDepth = 0
    maxTurn = 0
    while left <= right:
        mid = (left + right) // 2
        deep = 0
        for i in range(length):
            d = mid - food_times[i]
            if(d<0):
                d = 0
            deep += d
        turn = mid*length - deep

        if (turn < k):
            if turn > maxTurn:
                maxTurn = turn
                maxDepth = mid
            left = mid + 1
        elif (turn > k):
            right = mid - 1
        else:
            break
    turn = 0
    while food_times[turn] <= maxDepth:
        turn = (turn + 1) % length
    for i in range(k - maxTurn):
        food_times[turn] -= 1
        turn = (turn + 1) % length
        while food_times[turn] <= maxDepth:
            turn = (turn + 1) % length
    answer = turn + 1
    return answer

print(solution([5,1,3], 4))
print(solution([3,1,1,1,2,4,3],12))
print(solution([4,3,5,6,2], 7))
print(solution([10], 9))