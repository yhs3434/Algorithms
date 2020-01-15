# 프린터 큐
# https://www.acmicpc.net/problem/1966

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyQueue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def put(self, data):
        newNode = Node(data)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

    def get(self):
        if self.isEmpty():
            return -1
        retData = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return retData.data

    def getSize(self):
        return self.size

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.head.next.data

    def getBack(self):
        if self.isEmpty():
            return -1
        return self.tail.prev.data

    def getGreat(self):
        cur = self.head.next
        maxData = 0
        while cur.next != None:
            if cur.data[0] > maxData:
                maxData = cur.data[0]
            cur = cur.next
        return maxData

def solution(n, m, docs):
    q = MyQueue()
    for i in range(len(docs)):
        q.put((docs[i], i))
    dIdx = -1
    cnt = 0
    while dIdx != m:
        maxData = q.getGreat()
        cData = q.get()
        if cData[0] == maxData:
            dIdx = cData[1]
            cnt += 1
        else:
            q.put(cData)

    return cnt
t = int(input())
for xxx in range(t):
    n, m = map(int, input().split(' '))
    docs = list(map(int, input().split(' ')))
    print(solution(n, m, docs))