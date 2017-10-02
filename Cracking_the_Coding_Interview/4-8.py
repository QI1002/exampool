
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
        self.path = []
        self.datapath = []
        self.sum = 0

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
        print("{0}:{1},{2}:{3}:{4}".format(item.data, left, right, item.datapath, item.sum))
        if (item.left != 0): trace.push(item.left)
        if (item.right != 0): trace.push(item.right)

def traverseNode(root):
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

        item.path = path
        item.datapath = []
        for i in range(len(path)):
            item.datapath.append(path[i].data)
        item.sum = sum(item.datapath)

        if (item.left != 0):  trace.push((item.left, depth+1))
        if (item.right != 0): trace.push((item.right, depth+1))

def traverseSumNode(root):
    sumset = []
    sumpath = []
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

        item.path = path
        item.datapath = []
        for i in range(len(path)):
            item.datapath.append(path[i].data)
        item.sum = sum(item.datapath)

        for i in range(len(path)):
            summary = sum(item.datapath[i:])
            if (not summary in sumset):
                sumset.append(summary)
                sumpath.append(item.datapath[i:])

        if (item.left != 0):  trace.push((item.left, depth+1))
        if (item.right != 0): trace.push((item.right, depth+1))

    return sumset, sumpath

total = 22
target = genBinaryTree(list(range(total)))
printTree(target)
print("================")
traverseNode(target)
printTree(target)
print("================")
sumset, sumpath = traverseSumNode(target)
for i in range(len(sumset)):
    print("{0}:{1}".format(sumset[i], sumpath[i]));