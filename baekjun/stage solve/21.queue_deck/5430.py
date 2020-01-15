# AC
# https://www.acmicpc.net/problem/5430

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

    def showDeck(self):
        cur = self.head.next
        while cur.next != None:
            print(cur.data, end=' ')
            cur = cur.next
        print('')

def solution(orders, n, arr):
    if orders.count('D') > n:
        print('error')
        return
    answer = []
    d = MyDeck()
    for a in arr:
        d.push_back(a)
    flag = True
    for o in orders:
        if o == 'R':
            flag = not flag
        elif o == 'D':
            if flag:
                d.pop_front()
            else:
                d.pop_back()
    while not d.isEmpty():
        if flag:
            answer.append(d.pop_front())
        else:
            answer.append(d.pop_back())
    pStr = '['
    for a in answer:
        pStr += str(a)
        pStr += ','
    if pStr == '[':
        pStr = '[]'
    else:
        pStr = pStr[:-1]+']'
    print(pStr)


t = int(rl().rstrip())
for xxx in range(t):
    orders = rl().rstrip()
    n = int(rl().rstrip())
    arr = rl().rstrip()
    arr = arr[1:-1]
    if arr == '':
        arr = []
    else:
        arr = list(map(int, arr.split(',')))
    solution(orders, n, arr)