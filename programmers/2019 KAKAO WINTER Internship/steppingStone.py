def solution(stones, k):
    answer = 0

    left = 0
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        here = -1
        flag = True
        while here + k < len(stones):
            here = goAvail(here, stones, mid, k)
            if here == -1:
                flag = False
                break
        if flag:
            if mid > answer:
                answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

def goAvail(here, stones, water, k):
    limit = here + k
    idx = limit
    flag = False
    for i in range(limit, here, -1):
        if stones[i] >= water:
            idx = i
            flag = True
            break
    if flag:
        return idx
    else:
        return -1


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))