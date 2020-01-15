# 덱
# https://www.acmicpc.net/problem/10866

import sys
rl = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MyDeck:
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

    def push_front(self, data):
        newNode = Node(data)
        self.head.next.prev = newNode
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1

    def push_back(self, data):
        newNode = Node(data)
        self.tail.prev.next = newNode
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

    def pop_front(self):
        if self.isEmpty():
            return -1
        retData = self.head.next
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1
        return retData.data

    def pop_back(self):
        if self.isEmpty():
            return -1
        retData = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
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

n = int(input())
d = MyDeck()
for xxx in range(n):
    cOrder = rl().rstrip().split(' ')
    c = cOrder[0]
    if len(cOrder) == 2:
        if cOrder[0] == 'push_back':
            d.push_back(int(cOrder[1]))
        elif cOrder[0] == 'push_front':
            d.push_front(int(cOrder[1]))
    else:
        if c == 'pop_front':
            print(d.pop_front())
        elif c == 'pop_back':
            print(d.pop_back())
        elif c == 'size':
            print(d.getSize())
        elif c == 'empty':
            if d.isEmpty():
                print(1)
            else:
                print(0)
        elif c == 'front':
            print(d.getFront())
        elif c == 'back':
            print(d.getBack())