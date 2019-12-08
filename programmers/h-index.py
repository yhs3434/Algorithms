# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    maxVal = max(citations)

    for h in range(maxVal,0,-1):
        if(numHigh(citations, h)>=h):
            answer = h
            break

    return answer

def numHigh(citations, idx):
    i=-1
    j=0
    citationsCopy = [0 for i in range(len(citations))]
    while (i<len(citations)-1):
        i+=1
        if(citations[i]<idx):
            j+=1
    return len(citations)-j

print(solution([3, 0, 6, 1, 5]	))
print(solution([2,2, 2]	))