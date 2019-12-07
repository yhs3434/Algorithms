def bucketSort(A):
    B = [List() for i in range(len(A))]
    for a in A:
        idx = int(len(A)*a)
        B[idx].insert(a)
    for b in B:
        b.print()
        print(' ')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        headNode = Node(None)
        self.head = headNode

    def insert(self, data):
        newNode = Node(data)
        beforeNode = self.head
        curNode = self.head.next
        if (curNode==None):
            self.head.next = newNode
        else:
            while(curNode != None):
                if(curNode.data>newNode.data):
                    break
                beforeNode = curNode
                curNode = curNode.next
            if(curNode == None):
                beforeNode.next = newNode
            else:
                newNode.next = curNode
                beforeNode.next = newNode

    def print(self):
        curNode = self.head.next
        while(curNode!=None):
            print(curNode.data)
            curNode = curNode.next

bucketSort([0.78, 0.17,0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68])