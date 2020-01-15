# 큐 2
# https://www.acmicpc.net/problem/18258

import sys
rl = sys.stdin.readline

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

def solution(orders):
    q = MyQueue()

    for ord in orders:
        if len(ord)==2:
            q.push(ord[1])
        elif ord[0] == 'pop':
            print(q.pop())
        elif ord[0] == 'size':
            print(q.getSize())
        elif ord[0] == 'empty':
            if q.isEmpty():
                print(1)
            else:
                print(0)
        elif ord[0] == 'front':
            print(q.getFront())
        elif ord[0] == 'back':
            print(q.getBack())

n = int(rl())
orders = []
for xxx in range(n):
    orders.append(rl().rstrip().split(' '))
solution(orders)
