# 카드2
# https://www.acmicpc.net/problem/2164

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

    def push(self, data):
        newNode = Node(data)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

    def pop(self):
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

def solution(n):
    q = MyQueue()
    for i in range(1, n+1):
        q.push(i)
    while q.getSize()>1:
        q.pop()
        c = q.pop()
        q.push(c)

    return q.pop()

n = int(input())
print(solution(n))