# 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

from heapq import heappush, heappop

def solution(people, limit):
    answer = 0

    maxHeap = []
    minHeap = []
    length = len(people)

    for p in people:
        heappush(minHeap, p)
        heappush(maxHeap, -p)

    while (length>0):
        answer += 1
        maxPeople = -heappop(maxHeap)
        length -= 1
        weight = maxPeople
        while(length>0 and weight+minHeap[0]<=limit):
            minPeople = heappop(minHeap)
            length -= 1
            weight += minPeople

    return answer

print(solution([70, 50, 80, 50], 100))