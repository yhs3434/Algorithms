# 징검다리
# https://programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = float('inf')
    rockAmount = len(rocks)
    if(n==rockAmount):
        return distance

    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    dists = [rocks[i+1]-rocks[i] for i in range(len(rocks)-1)]
    left = min(dists)
    right = max(dists)

    while (left<=right):
        mid = (left+right)//2
        newDists = dists[:]
        j = 0
        count = 0
        while(j<len(newDists)):
            if(newDists[j] <= mid):
                if(j+1<len(newDists)):
                    newDists[j] += newDists[j+1]
                    del newDists[j+1]
                count += 1
            else:
                j += 1
        if (count>n):
            if(mid < answer):
                answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))