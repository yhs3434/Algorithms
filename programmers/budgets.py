# 예산
# https://programmers.co.kr/learn/courses/30/lessons/43237

def solution(budgets, M):
    answer = 0

    budgets.sort()
    length = len(budgets)

    left = 0
    right = length - 1
    mid = 0
    budget = 0

    while(left<=right):
        mid = (left+right)//2
        budget = getBudget(budgets, mid)
        if(budget<M):
            left = mid + 1
        elif(budget>M):
            right = mid - 1
        else:
            return budgets[mid]
    print(left, mid, right, budget, M)
    if(left>mid):
        if(mid==length-1):
            answer = budgets[mid]
        else:
            gap = M-budget
            rVol = length - mid -1
            answer = budgets[mid] + (gap // rVol)
    else:
        gap = budget - M
        rVol = length - mid
        if(gap%rVol==0):
            answer = budgets[mid] - (gap//rVol)
        else:
            answer = budgets[mid] - (gap // rVol) - 1
    return answer

def getBudget(budgets, idx):
    return sum(budgets[:idx]) + (len(budgets)-idx)*budgets[idx]

print(solution([120, 110, 140, 150],599))