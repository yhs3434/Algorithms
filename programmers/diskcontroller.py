# https://programmers.co.kr/learn/courses/30/lessons/42627
# 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0

    time = 0
    wait = []
    process = []
    count = 0

    for job in jobs:
        count += 1
        heapq.heappush(wait, (job[0], job[1]))

    while wait or process:
        if (len(process)==0 and time < wait[0][0]):
            time += 1
        else:
            while len(wait)>0 and time >= wait[0][0]:
                job = heapq.heappop(wait)

                heapq.heappush(process, (job[1], job[0]))
            if process:
                job = heapq.heappop(process)
                time += job[0]
                answer += time-job[1]

    return answer//count

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))