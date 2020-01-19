# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

import sys
rl = sys.stdin.readline
from heapq import heappush, heappop

class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 1
        self.left = None
        self.right = None

class midHeap:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, data):
        newNode = Node(data)
        if self.size == 0:
            self.root = newNode
        else:
            cur = self.root
            before = self.root

            while cur != None:
                cur.cnt += 1
                if newNode.data < cur.data:
                    before = cur
                    cur = cur.left
                else:
                    before = cur
                    cur = cur.right

            if newNode.data < before.data:
                before.left = newNode
            else:
                before.right = newNode
        self.size += 1

    def printAll(self):
        self.printData(self.root)

    def printData(self, node):
        if node == None:
            return
        self.printData(node.left)
        print(node.data, node.cnt)
        self.printData(node.right)

def findMid(mheap, mid):
    cur = mheap.root
    while mid > 0:
        if cur.left and cur.left.cnt >= mid:
            cur = cur.left
        else:
            if cur.left:
                mid -= cur.left.cnt
            if mid == 1:
                break
            elif mid > 1:
                mid -= 1
                cur = cur.right
    return cur.data

#mheap = midHeap()
maxHeap = []
minHeap = []

n = int(rl().rstrip())
for i in range(n):
    num = int(rl().rstrip())
    if i % 2 == 0:
        heappush(maxHeap, -num)
    else:
        heappush(minHeap, num)

    if minHeap and -maxHeap[0] > minHeap[0]:
        heappush(minHeap, -heappop(maxHeap))
        heappush(maxHeap, -heappop(minHeap))
    print(-maxHeap[0])