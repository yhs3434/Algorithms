import copy

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

def solution(n, m, arr):
    d = MyDeck()
    cnt = 0
    for i in range(1, n+1):
        d.push_back(i)
    while arr:
        if d.getFront() == arr[-1]:
            d.pop_front()
            arr.pop()
        else:
            d1 = copy.deepcopy(d)
            d2 = copy.deepcopy(d)
            cnt1 = 0
            cnt2 = 0
            while d1.getFront() != arr[-1]:
                cnt1 += 1
                d1.push_back(d1.pop_front())
            while d2.getFront() != arr[-1]:
                cnt2 += 1
                d2.push_front(d2.pop_back())
            if cnt1 < cnt2:
                while d.getFront() != arr[-1]:
                    cnt += 1
                    d.push_back(d.pop_front())
                arr.pop()
                d.pop_front()
            else:
                while d.getFront() != arr[-1]:
                    cnt += 1
                    d.push_front(d.pop_back())
                arr.pop()
                d.pop_front()
    return cnt

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.reverse()
print(solution(n, m, arr))