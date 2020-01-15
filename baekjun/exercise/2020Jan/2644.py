# 촌수계산
# https://www.acmicpc.net/problem/2644

class Node:
    def __init__(self, data):
        self.data = data
        self.p = None
        self.child = []

def findChild(cnt, node, data):
    if node.data == data:
        return cnt
    if len(node.child)==0:
        return -1
    for childNode in node.child:
        ca = findChild(cnt+1, childNode, data)
        if ca > 0:
            return ca
    return -1

n = int(input())
a, b = map(int, input().split(' '))
m = int(input())

node = [Node(i) for i in range(n+1)]
for xxx in range(m):
    x, y = map(int, input().split(' '))
    node[x].child.append(node[y])
    node[y].p = node[x]

deg = -1
cur = node[a]
cnt = 0
while cur != None:
    val = findChild(0, cur, b)
    if val != -1:
        deg = val
        break
    cur = cur.p
    cnt += 1
answer = 0
if deg == -1:
    answer = -1
else:
    answer = deg + cnt
print(answer)