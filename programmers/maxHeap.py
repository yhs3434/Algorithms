def __main__():
    maxHeap = Heap(20)
    print(maxHeap.get().data)
    print(maxHeap.get().data)
    maxHeap.put(3)
    maxHeap.put(6)
    maxHeap.put(5)
    maxHeap.put(4)
    print(maxHeap.get().data)
    print(maxHeap.get().data)
    print(maxHeap.get().data)
    maxHeap.put(13)
    maxHeap.put(16)
    maxHeap.put(15)
    maxHeap.put(14)
    print(maxHeap.get().data)
    print(maxHeap.get().data)



class Heap():
    def __init__(self, size):
        self.heap = [0 for i in range(size+1)]
        self.index = 0
        self.size = size

    def put(self, data):
        if(self.index==self.size):
            return False
        newNode = Node(data)
        self.index+=1
        self.heap[self.index] = newNode

        parentIndex = self.index//2
        curIndex = self.index
        while(curIndex > 1):
            if(self.heap[curIndex].data>self.heap[parentIndex].data):
                temp = self.heap[curIndex]
                self.heap[curIndex] = self.heap[parentIndex]
                self.heap[parentIndex] = temp
                curIndex = parentIndex
                parentIndex = parentIndex//2
            else:
                break

    def get(self):
        if(self.index == 0):
            return Node(False)
        returnNode = self.heap[1]
        self.heap[1] = self.heap[self.index]
        self.index -= 1
        curIndex = 1
        leftChildIndex = curIndex * 2
        rightChildIndex = curIndex * 2 + 1
        while(leftChildIndex<=self.index):
            if(leftChildIndex == self.index):
                temp = self.heap[curIndex]
                self.heap[curIndex] = self.heap[leftChildIndex]
                self.heap[leftChildIndex] = temp
                break
            else:
                if(self.heap[leftChildIndex].data>self.heap[rightChildIndex].data):
                    temp = self.heap[curIndex]
                    self.heap[curIndex] = self.heap[leftChildIndex]
                    self.heap[leftChildIndex] = temp
                    curIndex = leftChildIndex
                    leftChildIndex = curIndex*2
                    rightChildIndex = leftChildIndex+1
                else:
                    temp = self.heap[curIndex]
                    self.heap[curIndex] = self.heap[rightChildIndex]
                    self.heap[rightChildIndex] = temp
                    curIndex = rightChildIndex
                    leftChildIndex = curIndex*2
                    rightChildIndex = leftChildIndex+1
        return returnNode


class Node():
    def __init__(self, data):
        self.data = data

__main__()