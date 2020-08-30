def solution(N, stages):
    arrivals = [0] * (N+2)
    rates = [[i, 0] for i in range(N+1)]
    answer = []

    numOfUsers = len(stages)

    for stage in stages:
        arrivals[stage] += 1

    for i in range(1, N+1):
        if numOfUsers <= 0:
            break
        rates[i][1] = arrivals[i] / numOfUsers
        numOfUsers -= arrivals[i]

    rates.pop(0)
    rates.sort(key = lambda x: x[1], reverse=True)

    for rate in rates:
        answer.append(rate[0])

    return answer

print(solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))