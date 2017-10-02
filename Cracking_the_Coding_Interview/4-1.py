
class tree:
    def __init__(self, data, left = 0, right = 0):
        self.data = data
        self.left = left
        self.right = right

def max(a,b):
    if (a > b):
        return a
    else:
        return b

def treeDepth(target):
    if (target == 0):
        return 0

    depth1 = treeDepth(target.left)
    depth2 = treeDepth(target.right)
    return max(depth1,depth2)+1

def isBalance(target):
    if (target == 0):
        return True

    depth1 = treeDepth(target.left)
    depth2 = treeDepth(target.right)

    return abs(depth1-depth2) <= 1 and isBalance(target.left) and isBalance(target.right)


mytree = tree(0)
print("the balance tree is {0}".format(isBalance(mytree)))
mytree.left = tree(1)
print("the balance tree is {0}".format(isBalance(mytree)))
mytree.left.left = tree(2)
print("the balance tree is {0}".format(isBalance(mytree)))
mytree.left.right = tree(3)
print("the balance tree is {0}".format(isBalance(mytree)))
mytree.right = tree(4)
print("the balance tree is {0}".format(isBalance(mytree)))