def solution(scoville, K):
    answer = 0
    pq = PriorityQueue()
    for s in scoville:
        pq.push(s)

    while(pq.isEmpty()==False and pq.get()<K):
        data1 = pq.pop()
        data2 = None
        if(pq.isEmpty()==False):
            data2 = pq.pop()
        else:
            return -1
        newScoville = data1 + (data2 * 2)
        pq.push(newScoville)
        answer += 1

    return answer


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class PriorityQueue:
    def __init__(self):
        self.arr = [-1 for i in range(1000001)]
        self.idx = 0

    def push(self, data):
        self.idx += 1
        self.arr[self.idx] = data
        parent = self.idx // 2
        current = self.idx
        while(parent > 0):
            if(self.arr[current]<self.arr[parent]):
                temp = self.arr[parent]
                self.arr[parent] = self.arr[current]
                self.arr[current] = temp
            else:
                break

    def pop(self):
        retData = self.arr[1]
        self.arr[1] = self.arr[self.idx]
        self.idx -= 1

        current = 1
        leftChild = current*2
        rightChild = current*2 + 1
        while(leftChild<=self.idx):
            if(leftChild==self.idx):
                if(self.arr[current]>self.arr[leftChild]):
                    temp = self.arr[leftChild]
                    self.arr[leftChild] = self.arr[current]
                    self.arr[current] = temp
                break
            else:
                if(self.arr[leftChild] < self.arr[rightChild]):
                    if(self.arr[current]>self.arr[leftChild]):
                        temp = self.arr[leftChild]
                        self.arr[leftChild] = self.arr[current]
                        self.arr[current] = temp
                        current = leftChild
                    else:
                        break
                else:
                    if (self.arr[current] > self.arr[rightChild]):
                        temp = self.arr[rightChild]
                        self.arr[rightChild] = self.arr[current]
                        self.arr[current] = temp
                        current = rightChild
                    else:
                        break
                leftChild = current * 2
                rightChild = current * 2 + 1

        return retData

    def isEmpty(self):
        if(self.idx == 0):
            return True
        else:
            return False

    def get(self):
        if(self.isEmpty() == False):
            return self.arr[1]
        else:
            return None

    def print(self):
        for i in range(1, self.idx+1):
            print(self.arr[i], end=' ')
        print('')

print(solution([1, 2, 3, 9, 10, 12], 7))