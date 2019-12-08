def solution(budgets, M):
    answer = 0

    budgets.sort()

    top = budgets[-1]
    bot = budgets[0]
    mid = 0
    budget = 0

    while(top>bot):
        mid = (top + bot) // 2
        highIdx = whatIdx(budgets, mid)
        highValLen = len(budgets) - highIdx
        sum = 0

        for i in range(highIdx):
            sum += budgets[i]
        sum += (mid*highValLen)
        budget = sum
        if(budget<M):
            bot = mid+1
        elif(budget>M):
            top = mid-1
        else:
            break

    while(budget<M):
        temp = getBudget(budgets, mid+1)
        if(temp<=M):
            mid += 1
            budget = temp
        else:
            break
    while(budget>M):
        temp = getBudget(budgets, mid-1)
        if(temp>M):
            mid -= 1
            budget = temp
        else:
            break

    if(budget > M):
        mid -= 1
    elif(budget < M):
        if(getBudget(budgets, mid+1)<=M):
            mid += 1

    return mid

def whatIdx(budgets, val):
    idx = 0
    for budget in budgets:
        if(budget>=val):
            break
        idx += 1
    return idx

def getBudget(budgets, mid):
    highIdx = whatIdx(budgets, mid)
    highValLen = len(budgets) - highIdx
    sum = 0
    for i in range(highIdx):
        sum += budgets[i]
    sum += (mid * highValLen)
    return sum

print(solution([120, 110, 140, 150], 485))