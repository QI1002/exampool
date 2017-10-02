
def min(a,b):
    if (a > b):
        return b
    else:
        return a


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

def findNode(root, data):
    path = []
    depth = 0
    trace = stack()
    trace.push((root, depth))
    while(not trace.isEmpty()):
        v = trace.pop()
        item = v[0]
        depth = v[1]

        if (len(path) <= depth):
        	path.append(item)
        else:
        	path[depth] = item
        	path = path[0:depth+1]

        if (item.data == data):
            break

        # it's easy to extend the binary tree to multiple tree
        if (item.left != 0):  trace.push((item.left, depth+1))
        if (item.right != 0): trace.push((item.right, depth+1))

    return path

def findCommonParent(root, data1, data2):
    path1 = findNode(root, data1)
    path2 = findNode(root, data2)
    count = min(len(path1), len(path2))
    for i in range(count):
        if (path1[i] != path2[i]):
            return path1[i-1]

    return path1.pop()


total = 22
target = genBinaryTree(list(range(total)))
printTree(target)
value1 = 2
value2 = 8
ancestor = findCommonParent(target, value1, value2)
print("the common ancestor of {0} and {1} is {2}".format(value1, value2, ancestor.data))

