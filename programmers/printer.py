def solution(priorities, location):
    answer = 0

    q = Queue(100)
    idx = 0
    for p in priorities:
        q.push({'priority': p, 'location': idx})

        idx += 1

    while(q.isEmpty()==False):

        maxVal = q.maxVal()
        while(q.get()['priority']<maxVal):
            temp = q.pop()
            q.push(temp)

        answer += 1

        if(q.pop()['location']==location):
            break

    return answer



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

    def maxVal(self):
        curNode = self.root.next
        if(curNode==None):
            return None
        maxVal = -float('inf')
        while(curNode!=None):
            if(curNode.data['priority']>maxVal):
                maxVal = curNode.data['priority']
            curNode = curNode.next
        return maxVal

solution([1, 1, 9, 1, 1, 1], 0)