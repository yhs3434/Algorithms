import heapq

def solution(scoville, K):
    answer = 0
    pq = []
    for s in scoville:
        heapq.heappush(pq, s)

    while(len(pq)!=0):
        data1 = heapq.heappop(pq)
        if(data1 >= K):
            break
        data2 = None
        if(len(pq)!=0):
            data2 = heapq.heappop(pq)
        else:
            return -1
        newScoville = data1 + (data2 * 2)
        heapq.heappush(pq, newScoville)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))