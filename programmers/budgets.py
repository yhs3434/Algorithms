def solution(budgets, M):
    answer = 0

    budgets.sort()
    length = len(budgets)

    left = 0
    right = length - 1
    budget = 0

    while(left<=right):
        mid = (left+right)//2
        budget = sum(budgets[:mid])+(length-mid)*budgets[mid]
        if(budget<M):
            left = mid + 1
        elif(budget>M):
            right = mid - 1
        else:
            return budgets[mid]
    gap = budget - M
    if(left>=length):
        return budgets[left-1]
    elif(right<0):
        return budgets[left] + ((-gap)//(length-left))
    if(gap >= 0):
        answer = budgets[left] - (gap//(length-left)) - 1
    else:
        answer = budgets[left] + ((-gap)//(length-left))
    return answer

print(solution([120, 110, 140, 150,170,200,130], 399))