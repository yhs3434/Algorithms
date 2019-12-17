class Node:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.p = None
        self.left = None
        self.right = None
        self.size = 0

class RBTree:
    def __init__(self):
        self.none = Node(None, None)
        self.root = self.none

    def insert(self, key):
        z = Node('RED', key)
        z.left = self.none
        z.right = self.none

        y = self.none
        x = self.root
        while(x!=self.none):
            y = x
            if(z.key < x.key):
                x = x.left
            else:
                x = x.right
        if(y == self.none):
            self.root = z
            z.p = self.none
        else:
            if(x == y.left):
                y.left = z
            else:
                y.right = z
            z.p = y
        self.insertFixup(z)

    def insertFixup(self, z):
        while(z.p.color == 'RED'):
            if(z.p == z.p.p.left):
                y = z.p.p.right
                if(y.color == 'RED'):
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                else:
                    if(z==z.p.right):
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.rightRotate(z.p.p)
            else:
                y=z.p.p.left
                if(y.color == 'RED'):
                    y.color = 'BLACK'
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z=z.p.p
                else:
                    if(z==z.p.left):
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.leftRotate(z.p.p)
        self.root.color = 'BLACK'

    def leftRotate(self, z):
        x = z.left
        y = z.right

        z.right = y.left
        if(y.left != self.none):
            z.right.p = z
        if(z.p == self.none):
            self.root = y
            y.p = self.none
        else:
            if(z==z.p.left):
                z.p.left = y
                y.p = z.p
            else:
                z.p.right = y
                y.p = z.p
        y.left = z
        z.p = y

    def rightRotate(self, z):
        y = z.left

        z.left = y.right
        if(y.right != self.none):
            y.right.p = z
        y.p = z.p
        if(z == self.root):
            self.root = y
        else:
            if(z==z.p.left):
                z.p.left = y
            else:
                z.p.right = y
        z.p =y
        y.right = z

    def transplant(self, u, v):
        if (u == self.root):
            self.root = v
        else:
            if(u==u.p.left):
                u.p.left = v
            else:
                u.p.right = v
        v.p = u.p

    def treeMinimum(self, x):
        y = x
        while(x != self.none):
            y = x
            x = x.left
        return y

    def delete(self, z):
        y = z
        yOriginalColor = y.color
        if (z.left == self.none):
            x = z.right
            self.transplant(z, x)
        elif (z.right == self.none):
            x = z.left
            self.transplant(z, x)
        else:
            y = self.treeMinimum(z.right)
            yOriginalColor = y.color
            x = y.right
            if(y == z.right):
                y.p = z.p
            else:
                self.transplant(y, x)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if(yOriginalColor == 'BLACK'):
            self.deleteFixup(x)

    def deleteFixup(self, x):
        while (x!=self.root and x.color == 'BLACK'):
            if(x == x.p.left):
                y = x.p.right
                if(y.color == 'RED'):
                    y.color = 'BLACK'
                    x.p.color = 'RED'
                    self.leftRotate(x.p)
                    y = x.p.right
                else:
                    if(y.left.color == 'BLACK' and y.right.color == 'BLACK'):
                        y.color = 'RED'
                        x= x.p
                    else:
                        if(y.right.color == 'BLACK'):
                            y.left.color = 'BLACK'
                            y.color = 'RED'
                            self.righgtRotate(y)
                            y = x.p.right
                        y.color = x.p.color
                        x.p.color = 'BLACK'
                        y.right.color = 'BLACK'
                        self.leftRotate(x.p)
                        x = self.root
            else:
                y = x.p.left
                if(y.color == 'RED'):
                    y.color = 'BLACK'
                    x.p.color = 'RED'
                    self.rightRotate(x.p)
                    y = x.p.left
                else:
                    if(y.left.color == 'BLACK' and y.right.color == 'BLACK'):
                        y.color = 'RED'
                        x = x.p
                    else:
                        if(y.left.color == 'BLACK'):
                            y.right.color = 'BLACK'
                            y.color = 'RED'
                            self.leftRotate(y)
                            y = x.p.left
                        y.color = y.p.color
                        y.p.color = 'BLACK'
                        y.left.color = 'BLACK'
                        self.rightRotate(x.p)
                        x = self.root
        x.color = 'BLACK'

    def initSize(self, x):
        if(x==self.none):
            return 0
        x.size = self.initSize(x.left) + self.initSize(x.right) + 1
        return x.size

    def select(self, x, i):
        self.initSize(self.root)
        return self.doSelect(x, i)

    def doSelect(self, x, i):
        r = x.left.size + 1
        if(r==i):
            return x
        else:
            if (i<r):
                return self.select(x.left, i)
            else:
                return self.select(x.right, i-r)

    def rank(self, x):
        r = x.left.size + 1
        y = x
        while (y!=self.root):
            if(y!=y.p.left):
                r += (y.p.left.size + 1)
            y = y.p
        return r