def solution(progresses, speeds):
    answer = []

    q = Queue(100)

    for i in range(len(progresses)):
        q.push({'progress': progresses[i], 'speed': speeds[i]})

    time = 0
    while(q.isEmpty()==False):
        comTime = getTime(q.pop())
        count = 1
        while(getTime(q.get())<=comTime):
            q.pop()
            count+=1
        answer.append(count)

    return answer

def getTime(data):
    if(data == None):
        return float('inf')
    progress = data['progress']
    speed = data['speed']
    time = (100 - progress)//speed
    if((100-progress)%speed!=0):
        time += 1
    return time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, size):
        self.root = Node(0)
        self.maxSize = size
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        curNode = self.root.next
        befNode = self.root
        while(curNode!=None):
            befNode = curNode
            curNode = curNode.next
        befNode.next = newNode
        self.size += 1

    def pop(self):
        curNode = self.root.next
        befNode = self.root
        befNode.next = curNode.next
        if(curNode == None):
            return None
        else:
            self.size -= 1
            return curNode.data

    def get(self):
        curNode = self.root.next
        if(curNode==None):
            return None
        else:
            return curNode.data

    def isEmpty(self):
        if(self.size>0):
            return False
        else:
            return True

solution([93,30,55], [1,30,5])