def solution(numbers):
    answer = ''
    nums = ['']
    num = ''
    q = Queue()
    q.enqueue('')
    for n in numbers:
        temp = []
        while(q.isEmpty()!=True):
            num = q.dequeue()
            for i in range(len(num)+1):
                newNum = num[:i]+str(n)+num[i:]
                if (len(temp)==0):
                    temp.append(newNum)
                else:
                    if(newNum>temp[0]):
                        temp[0] = newNum
        print(temp)
        q.enqueue(temp[0])
    answers = []
    while(q.isEmpty()!=True):
        answers.append(int(q.dequeue()))
    answers.sort(reverse=True)
    answer = str(answers[0])
    return answer

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def enqueue(self, data):
        newNode = Node(data)
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

    def get(self):
        if(self.size==0):
            return None
        return self.tail.prev.data

    def isEmpty(self):
        if(self.size==0):
            return True
        else:
            return False


print(solution([3, 30, 34, 5, 9]))