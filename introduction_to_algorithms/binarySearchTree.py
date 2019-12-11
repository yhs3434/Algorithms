class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        newNode = Node(key)
        if(self.root == None):
            self.root = newNode
        else:
            cur = self.root
            bef = self.root.p
            while(cur!=None):
                bef = cur
                if(key==cur.key):
                    return
                elif(key<cur.key):
                    cur=cur.left
                elif(key>cur.key):
                    cur=cur.right
            if(key < bef.key):
                bef.left = newNode
                newNode.p = bef
            else:
                bef.right = newNode
                newNode.p = bef

    def delete(self, key):
        x = self.root
        while(x!=None):
            if (x.key == key):
                break
            elif(key < x.key):
                x = x.left
            else:
                x = x.right
        if(x==None):
            return None
        if(x.left == None and x.right == None):
            self.transplant(x, x.right)
        elif(x.left == None or x.right == None):
            if(x.left == None):
                self.transplant(x, x.right)
            else:
                self.transplant(x, x.left)
        else:
            y = self.treeMinimum(x.right)
            if (y.p!=x):
                self.transplant(y, y.right)
                y.right = x.right
                y.right.p = y
            self.transplant(x, y)
            y.left = x.left
            y.left.p = y
        return

    def treeMinimum(self, x):
        while(x.left != None):
            x = x.left
        return x

    def treeMaximum(self, x):
        while(x.right != None):
            x = x.right
        return x

    def nextNode(self, x):
        if(x.right != None):
            return self.treeMinimum(x.right)
        y = x.p
        while (y!=None and x==y.right):
            x = y
            y = y.p
        return y

    def transplant(self, x, y):
        if(x.p==None):
            self.root = y
        else:
            if(x.p.left == x):
                x.p.left = y
            else:
                x.p.right = y
            if(y!=None):
                y.p = x.p

    def print(self):
        self.midOrder(self.root)
        print('')
        return

    def midOrder(self, node):
        if(node==None):
            return
        self.midOrder(node.left)
        print(node.key, end=' ')
        self.midOrder(node.right)

bst = BST()

bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)

bst.print()

bst.delete(5)
bst.delete(1)
bst.delete(2)
bst.delete(4)
bst.print()
bst.delete(3)
bst.print()
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.delete(5)
bst.delete(1)
bst.delete(2)
bst.delete(4)
bst.insert(7)
bst.insert(8)
bst.insert(10)
bst.insert(12)
bst.insert(11)
bst.insert(5)
bst.insert(2)
bst.insert(4)
bst.print()
bst.delete(7)
bst.delete(8)
bst.delete(10)
bst.delete(11)
bst.delete(5)
bst.insert(2)
bst.print()
