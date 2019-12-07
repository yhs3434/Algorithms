import heapq

def solution(jobs):
    answer = 0

    heap = []
    count = 0
    time = 0

    for j in jobs:
        heapq.heappush(heap, (j[1], j[0]))
        count += 1
    temp = []
    beforeTime = 0
    while heap:
        job = heapq.heappop(heap)
        if(job[1]>time):
            temp.append(job)
        else:
            time += (job[0])
            answer += (time-job[1])
            for t in temp:
                heapq.heappush(heap, t)
            temp=[]
        if(time == beforeTime):
            print(time, beforeTime)
            heapq.heappush(heap, job)
            time += 1
        beforeTime = time

    return answer//count

print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))