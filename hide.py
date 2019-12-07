def solution(clothes):
    answer = 1

    q = Queue()

    map = {}
    for cloth in clothes:
        if(cloth[1] not in map):
            map[cloth[1]] = 1
        else:
            map[cloth[1]] += 1

    for key in map:
        answer *= (map[key]+1)
    answer -= 1
    return answer

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, key, data):
        newNode = Node(key, data)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1

    def dequeue(self):
        if(self.size == 0):
            return None
        retNode = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        return retNode.data

    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))