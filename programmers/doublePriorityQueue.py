# 이중 우선순위 큐
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    answer = []

    maxHeap = []
    minHeap = []
    count = 0

    for operation in operations:
        if(operation[0]=="I"):
            val = int(operation[2:])
            heapq.heappush(maxHeap, -val)
            heapq.heappush(minHeap, val)
            count += 1
        else:
            if (count > 0):
                if(operation[2]=='1'):
                    val = heapq.heappop(maxHeap)
                    minHeap.remove(-val)
                else:
                    val = heapq.heappop(minHeap)
                    maxHeap.remove(-val)
                count -= 1

    if(count == 0):
        answer = [0, 0]
    else:
        answer.append(-heapq.heappop(maxHeap))
        answer.append(heapq.heappop(minHeap))

    return answer

print(solution(['I 7','I 5','I -5','D -1', 'D 1', 'I 4']))