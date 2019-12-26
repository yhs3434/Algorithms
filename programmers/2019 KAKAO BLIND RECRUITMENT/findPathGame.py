# 2019 KAKAO BLIND RECRUITMENT 길 찾기 게임
# https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = [[], []]
    length = len(nodeinfo)
    for i in range(1, length + 1):
        nodeinfo[i-1].append(i)

    nodeinfo.sort(key = lambda key: key[0])
    nodeinfo.sort(key = lambda key: key[1], reverse=True)
    nodeinfo.reverse()
    before = None
    tree = BinaryTree()

    while nodeinfo:
        cur = nodeinfo.pop()
        newNode = Node(cur[2], [cur[0], cur[1]])
        tree.insert(newNode)
    tree.preOrder(tree.root, answer[0])
    tree.lastOrder(tree.root, answer[1])
    return answer

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, node):
        if(self.root == None):
            self.root = node
        else:
            before = None
            cur = self.root
            while cur!=None:
                before = cur
                if (node.data[0] < cur.data[0]):
                    cur = cur.left
                else:
                    cur = cur.right

            if(node.data[0] < before.data[0]):
                node.p = before
                before.left = node
            else:
                node.p = before
                before.right = node

    def preOrder(self, node, arr):
        if (node == None):
            return
        self.printNode(node, arr)
        self.preOrder(node.left, arr)
        self.preOrder(node.right, arr)

    def lastOrder(self, node, arr):
        if (node == None):
            return
        self.lastOrder(node.left, arr)
        self.lastOrder(node.right, arr)
        self.printNode(node, arr)

    def printNode(self, node, arr):
        arr.append(node.key)



print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))