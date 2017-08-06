
class stack:
    def __init__(self):
        self.body = []

    def push(self, data):
        self.body.append(data)

    def pop(self):
        if (len(self.body) == 0):
            return None
        else:
            return self.body.pop()

    def isEmpty(self):
        return True if len(self.body) == 0 else False

class tree:
    def __init__(self, data, left = 0, right = 0):
        self.data = data
        self.left = left
        self.right = right

def genBinaryTree(data):
    count = len(data)
    if (count == 0):
        return 0
    else:
        half = count // 2
        root = tree(data[half])
        root.left = genBinaryTree(data[0:half])
        root.right = genBinaryTree(data[half+1:])  
        return root
        
def printTree(root):
    trace = stack()
    trace.push(root)
    while(not trace.isEmpty()):
        item = trace.pop()
        left = "NULL" if item.left == 0 else item.left.data
        right = "NULL" if item.right == 0 else item.right.data
        print("{0}:{1},{2}".format(item.data, left, right))
        if (item.left != 0): trace.push(item.left)            
        if (item.right != 0): trace.push(item.right)
        
target = genBinaryTree(list(range(7)))
printTree(target)