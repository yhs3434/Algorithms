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
    gap = budget - M
    print(budget, M)
    if(gap >= 0):
        if(mid>=(length-1)):
            return budgets[-1]
        answer = budgets[mid+1] - (gap//(length-mid+1)) - 1
    else:
        answer = budgets[mid] + ((-gap)//(length-mid))
    return answer

def getBudget(budgets, idx):
    return sum(budgets[:idx]) + (len(budgets)-idx)*budgets[idx]

print(solution([120, 110, 140, 150],500))