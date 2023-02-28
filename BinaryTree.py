# odnosvyazniy spisok

class Node:
    def __init__(self, data, left = None, right = None, height = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.height = height
        self.parent = parent

    def update(self):
        if self.right is None and self.left is None:
            self.height = 0
            #return
        elif (self.right is None) != (self.left is None):
            if (self.right is None):
                self.left.update()
                self.height = self.left.height + 1
            else:
                self.right.update()
                self.height = self.right.height + 1
        else:
            self.left.update()
            self.right.update()
            self.height = max(self.left.height, self.right.height) + 1


class BinaryTree:
    head = None


    def __init__(self, head=None, theheight = None):
        self.head = head

        self.listik = []

    def plus(self, data):
        self.add(data, self.head)
        self.head.update()


    def add(self, data, newnode):
        if self.head is None:
            self.head = Node(data)
            self.head.height = 0
        else:
            if data >= newnode.data:
                if newnode.right is None:
                    newnode.right = Node(data)
                    newnode.right.parent = newnode
                    newnode.right.height = 0
                    newnode.right.right = None
                    newnode.right.left = None


                else:
                    self.add(data, newnode.right)
            else:
                if newnode.left is None:
                    newnode.left = Node(data)
                    newnode.left.parent = newnode
                    newnode.left.height = 0
                    newnode.left.right = None
                    newnode.left.left = None


                else:
                    self.add(data, newnode.left)


    def delete(self, key):
        self.erase(key, tree.head)

    def write(self, newnode):
        if newnode.left is not None:
            self.write(newnode.left)
        print(newnode.data)
        if newnode.right is not None:
            self.write(newnode.right)

    def erase(self, key, newnode):

        while newnode.data != key:
            if key >= newnode.data:
                if newnode.right is not None:
                    newnode = newnode.right
                else:
                    return -1
            else:
                if newnode.left is not None:
                    newnode = newnode.left
                else:
                    return -1
        if newnode.left is None and newnode.right is None:
            if newnode.data >= newnode.parent.data:
                newnode.parent.right = None
            else:
                newnode.parent.left = None
            return 1
        elif (newnode.left is not None and newnode.right is None) or (newnode.left is None and newnode.right is not None):
            if (newnode.left is not None and newnode.right is None):
                if newnode.data >= newnode.parent.data:
                    newnode.parent.right = newnode.left
                else:
                    newnode.parent.left = newnode.left
            else:
                if newnode.data >= newnode.parent.data:
                    newnode.parent.right = newnode.right
                else:
                    newnode.parent.left = newnode.right
            return 1
        else:
            somenode = newnode.right
            while somenode.left is not None:
                somenode = somenode.left
            newnode.data = somenode.data
            self.erase(somenode.data, somenode)
        return -1



    def find(self, key):
        newnode = self.head
        while newnode.data != key:
            if newnode.data < key:
                if newnode.left is not None:
                    newnode = newnode.left
                else:
                    return 0
            else:
                if newnode.right is not None:
                    newnode = newnode.right
                else:
                    return 0
        return 1



tree = BinaryTree()

tree.plus(8)
tree.plus(4)
tree.plus(2)
tree.plus(1)
tree.plus(3)
tree.plus(6)
tree.plus(5)
tree.plus(7)
tree.plus(12)
tree.plus(10)
tree.plus(14)
tree.plus(9)
tree.plus(11)
tree.plus(13)
tree.plus(15)
print(tree.head.data)
tree.delete(8)
try:
    print(tree.head.data)
    print(tree.head.right.data)
except:
    print("Oopsie")