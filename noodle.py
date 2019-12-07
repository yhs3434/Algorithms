import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    dates.reverse()
    supplies.reverse()
    while stock<k:
        while len(dates)>0 and dates[-1] <= stock:
            heapq.heappush(heap, -supplies.pop())
            dates.pop()
        stock += (-heapq.heappop(heap))
        answer += 1

    return answer

print(solution(4, [1,2,3,4], [10,40,30,20], 100))