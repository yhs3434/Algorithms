def solution(bridge_length, weight, truck_weights):
    answer = 0
    time = []

    q = Queue()

    answer += 1
    idx = 0
    q.push(truck_weights[idx])
    idx += 1
    time.append(bridge_length)
    while(q.isEmpty()!=True):
        answer += 1
        minusOne(time)
        if (min(time) <= 0):
            del time[0]
            q.pop()
        if(idx<len(truck_weights)):
            if(q.weight()+truck_weights[idx]<=weight):
                q.push(truck_weights[idx])
                time.append(bridge_length)
                idx += 1

    return answer

def minusOne(arr):
    for i in range(len(arr)):
        arr[i] -= 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.root = Node(None)
        self.size = 0

    def push(self, data):
        curNode = self.root.next
        befNode = self.root

        while(curNode!=None):
            befNode = curNode
            curNode = curNode.next

        befNode.next = Node(data)
        self.size += 1

    def pop(self):
        if(self.size == 0):
            return None
        retNode = self.root.next
        self.root.next = self.root.next.next
        self.size -= 1
        return retNode.data

    def get(self):
        if(self.size == 0):
            return None
        return self.root.next.data

    def isEmpty(self):
        if(self.size == 0):
            return True
        else:
            return False

    def weight(self):
        weight = 0
        curNode = self.root.next
        while(curNode!=None):
            weight += curNode.data
            curNode = curNode.next
        return weight

solution(2, 10,[7,4,5,6])