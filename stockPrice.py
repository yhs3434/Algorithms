import queue

def solution(prices):
    pq = queue.PriorityQueue()
    stockTime = [-i-1 for i in range(len(prices))]
    stockFlag = [False for i in range(len(prices))]
    for i in range(len(prices)):
        addFunc(stockTime, stockFlag)
        if(pq.qsize()>0):
            curVal = prices[i]
            curIndex = i
            while(pq.qsize()>0):
                print(pq.qsize())
                tempTuple = pq.get()
                tempVal = -tempTuple[0]
                tempIndex = tempTuple[1]
                if(curVal<tempVal):
                    stockFlag[tempIndex] = True
                else:
                    pq.put(tempTuple)
                    break

            pq.put((-prices[i], i))
        else:
            pq.put((-prices[i], i))
    return stockTime

def addFunc(time, flag):
    for i in range(len(time)):
        if(flag[i]==False):
            time[i] += 1

print(solution([1, 2, 3, 2, 3,1, 2, 3, 2, 3,1, 2, 3, 2, 3]))