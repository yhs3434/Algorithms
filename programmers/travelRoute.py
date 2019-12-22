# 여행경로
# https://programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []

    stack = [["ICN",[]]]
    length = len(tickets)
    start = "ICN"
    end = ""
    availRoutes = []

    while stack:
        curPtr = stack.pop()
        curStart = curPtr[0]
        if(len(curPtr[1]) == length):
            availRoutes.append(["ICN"])
            for i in range(length):
                availRoutes[len(availRoutes)-1].append(curPtr[1][i][1])
        for i in range(length):
            if (tickets[i][0] == curStart):
                if(curPtr[1].count(tickets[i])<tickets.count(tickets[i])):
                    stack.append([tickets[i][1], curPtr[1]+[tickets[i]]])

    availRoutes.sort()
    answer = availRoutes[0]
    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))