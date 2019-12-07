def solution(baseball):
    availables = []
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if(i!=j and i!=k and j!=k):
                    num = ""
                    num += str(i)
                    num += str(j)
                    num += str(k)
                    availables.append(num)

    st = Stack()
    st.push(availables)
    for b in baseball:
        availables = st.pop().data
        newAvailables = []
        for a in availables:
            if(throwBall(a, str(b[0])) == [b[1], b[2]]):
                newAvailables.append(a)
        st.push(newAvailables)
    answer = len(st.pop().data)

    return answer

def throwBall(num1, num2):
    strike = 0
    ball = 0

    for i in range(3):
        if(num1[i]==num2[i]):
            strike += 1
    for i in range(3):
        for j in range(3):
            if(i==j):
                continue
            else:
                if(num1[i]==num2[j]):
                    ball += 1
    return [strike, ball]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        headNode = Node(None)
        self.head = headNode

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head.next
        self.head.next = newNode

    def pop(self):
        returnNode = self.head.next
        if(returnNode != None):
            self.head.next = self.head.next.next
        return returnNode

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])