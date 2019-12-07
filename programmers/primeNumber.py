def solution(numbers):
    answer = 0
    st = Stack()
    st.push("")
    for n in numbers:
        temp = []
        while(st.isEmpty()==False):
            data = st.pop()
            for i in range(len(data)+1):
                data2 = data[:i]+n+data[i:]
                data3 = data[:i]+'x'+data[i:]
                if(data2 not in temp):
                    temp.append(data2)
                if(data3 not in temp):
                    temp.append(data3)

        for t in temp:
            st.push(t)
    arr = []
    while(st.isEmpty()==False):
        arr.append(st.pop())
    arr = removeNotNum(arr)
    primeCount = 0
    for a in arr:
        if(isPrime(a)):
            primeCount+=1
    answer = primeCount
    return answer

def isPrime(num):
    flag = True
    for i in range(2, int(num**(1/2))+1):
        if((num%i)==0):
            flag=False
            break
    return flag

def removeNotNum(arr):
    newArr = []
    for a in arr:
        newNum = a.replace('x','')
        if(newNum==''):
            continue
        newNum = int(newNum)
        if(newNum not in newArr and newNum>1):
            newArr.append(newNum)
    return newArr

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
        data = None
        if(returnNode!=None):
            data = returnNode.data
        return data

    def isEmpty(self):
        if(self.head.next==None):
            return True
        else:
            return False

print(solution('17'))