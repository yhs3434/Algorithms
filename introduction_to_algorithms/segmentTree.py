class Node:
    def __init__(self, color, seg):
        self.p = None
        self.left = None
        self.right = None
        self.color = color
        self.key = seg[0]
        self.int = seg
        self.max = seg[-1]

class RedBlackTree:
    def __init__(self):
        self.none = Node('BLACK', None, [0])
        self.root = self.none

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if(y.left != self.none):
            y.left.p = x
        y.p = x.p
        if(x.p == self.none):
            self.root = y
        else:
            if(x.p.left == x):
                x.p.left = y
            else:
                x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        if (x.right != None):
            x.right.p = y
        x.p = y.p
        if(y.p == None):
            self.root = x
        else:
            if (y.p.left == y):
                y.p.left = x
            else:
                y.p.right = x
        y.p = x
        x.right = y

    def insert(self, z):
        y = self.none
        x = self.root
        while (x != self.none):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.p = y
        if (x == self.none):
            self.root = z
        else:
            if(z.key < y.key):
                y.left = z
            else:
                y.right = z
        z.left = self.none
        z.right = self.none
        z.color = 'RED'
        self.insertFixup(z)

    def insertFixup(self, z):
        while (z.p.color == 'RED'):
            if (z.p == z.p.p.left):
                y = z.p.p.right
                if(y.color == 'RED'):
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if(z == z.p.right):
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if (y.color == 'RED'):
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if (z == z.p.left):
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.leftRotate(z.p.p)
        self.root.color = 'BLACK'

    def transplant(self, u, v):
        if (u.p == self.none):
            self.root = v
        else:
            if(u == u.p.left):
                u.p.left = v
            else:
                u.p.right = v
        v.p = u.p

    def treeMinimum(self, z):
        y = z.p
        while (z != self.none):
            y = z
            z = z.left
        return y

    def delete(self, z):
        y = z
        yOriginalColor = y.color
        if (z.left == self.none):
            x = z.right
            self.transplant(z, z.right)
        elif (z.right == self.none):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            yOriginalColor = y.color
            x = y.right
            if (y.p == z):
                x.p = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if(yOriginalColor == 'BLACK'):
            self.deleteFixup(x)

    def deleteFixup(self, x):
        while (x!=self.root and x.color=='BLACK'):
            if (x==x.p.left):
                w = x.p.right
                if(w.color=='RED'):
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.leftRotate(x.p)
                    w = x.p.right
                if(w.left.color == 'BLACK' and w.right.color == 'BLACK'):
                    w.color = 'RED'
                    x = x.p
                else:
                    if (w.left.color == 'RED' and w.right.color == 'BLACK'):
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.rightRotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    w.p.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.leftRotate(w.p)
                    x = self.root
            else:
                w = x.p.left
                if(w.color == 'RED'):
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.rightRotate(x.p)
                    w = x.p.left
                if(w.left.color == 'BLACK' and w.right.color == 'BLACK'):
                    w.color = 'RED'
                    x= x.p
                else:
                    if(w.left.color == 'BLACK' and w.right.color == 'RED'):
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.leftRotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    w.left.color = 'BLACK'
                    w.p.color = 'BLACK'
                    self.rightRotate(w.p)
                    x = self.root
        x.color = 'BLACK'

    def initMax(self, x):
        if(x == self.none):
            return 0
        x = self.root
        x.max = max(x.int[-1], self.initMax(x.left), self.initMax(x.right))
        return x.max

    def intervalSearch(self, i):
        x = self.root
        while (x!=self.none and self.isOverlap(i, x.int)==False):
            if (x.left != self.none and x.left.max >= i[0]):
                x = x.left
            else
                x = x.right
        return x

    def isOverlap(self, x, y):
        flag = False
        if(x[0] in y):
            flag = True
        elif(x[-1] in y):
            flag = True
        return flag