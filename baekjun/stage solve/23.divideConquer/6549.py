# 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549

import sys
sys.setrecursionlimit(10**6)
rl = sys.stdin.readline

class Node:
    def __init__(self, l, r, histogram):
        self.histogram = histogram
        self.range = (l, r)
        self.size = r - l + 1
        self.height = min(self.histogram[l: r+1])
        self.maxHeight = max(self.histogram[l: r+1])
        self.area = self.size * self.height
        self.left = None
        self.right = None

    def split(self, answer):
        if self.area > answer[0]:
            answer[0] = self.area

        l = self.range[0]
        r = self.range[1] + 1
        if r <= 1:
            return
        if self.height == self.maxHeight:
            return
        m = l
        for i in range(l, r):
            if self.histogram[i] == self.height:
                break
            m += 1
        if m < r:
            if l < m:
                leftNode = Node(l, m-1, self.histogram)
                #self.left = leftNode
                leftNode.split(answer)
            if m+1 < r:
                rightNode = Node(m+1, r-1, self.histogram)
                #self.right = rightNode
                rightNode.split(answer)

    def maxArea(self, answer):
        if self.area > answer[0]:
            answer[0] = self.area
        if self.left != None:
            self.left.maxArea(answer)
        if self.right != None:
            self.right.maxArea(answer)

def solutionSegmentTree(histo):
    node = Node(0, len(histo)-1, histo)
    answer = [0]
    node.split(answer)

    #node.maxArea(answer)
    return answer[0]

def solution(histo):
    answer = 0
    st = []
    i = 0
    while i < len(histo):
        if not st:
            st.append(i)
            i += 1
        else:
            if histo[i] >= histo[st[-1]]:
                st.append(i)
                i += 1
            else:
                st.pop()
                cArea = 0
                if st:
                    cArea = getArea(st[-1]+1, i-1, histo)
                else:
                    cArea = getArea(0, i-1, histo)
                if cArea > answer:
                    answer = cArea
    while st:
        st.pop()
        cArea = 0
        if st:
            cArea = getArea(st[-1] + 1, i - 1, histo)
        else:
            cArea = getArea(0, i - 1, histo)
        if cArea > answer:
            answer = cArea

    return answer

histo_g = []

def getArea(l, r, h):
    #h = min(histo_g[l: r+1])
    w = r - l + 1
    return h*w

while True:
    N, *histo = list(map(int, rl().rstrip().split(' ')))
    if N == 0:
        break
    histo_g = histo
    answer = 0
    st = []
    i = 0
    minh = float('inf')
    while i < len(histo):
        if not st:
            minh = float('inf')
            st.append(i)
            i += 1
        else:
            if histo[i] >= histo[st[-1]]:
                minh = float('inf')
                st.append(i)
                i += 1
            else:
                ci = st.pop()
                if histo_g[ci] < minh:
                    minh = histo_g[ci]
                cArea = 0
                if st:
                    cArea = getArea(st[-1] + 1, i - 1, minh)
                else:
                    cArea = getArea(0, i - 1, minh)
                if cArea > answer:
                    answer = cArea
    minh = float('inf')
    while st:
        ci = st.pop()
        if histo_g[ci] < minh:
            minh = histo_g[ci]
        cArea = 0
        if st:
            cArea = getArea(st[-1] + 1, i - 1, minh)
        else:
            cArea = getArea(0, i - 1, minh)
        if cArea > answer:
            answer = cArea

    print(answer)