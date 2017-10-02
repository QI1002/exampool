
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
        self.next = 0

def printlist(head):
    n = head
    while(n != 0):
        print(n.data)
        n = n.next

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

def treeDepth(target):
    if (target == 0):
        return 0

    depth1 = treeDepth(target.left)
    depth2 = treeDepth(target.right)
    return max(depth1,depth2)+1

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

def addlink(item, depth, result):
    if (len(result) == depth):
        result.append([])

    result[depth].append(item)

def addlink2(item, depth, result):
    if (len(result) == depth):
        result.append(item)
    else:
        item.next = result[depth]
        result[depth] = item

def linkTranveseTree(root, isLink = False):

    add = addlink2 if isLink else addlink
    result = []
    depth = 0
    trace = stack()
    trace.push((root, depth))
    add(root, depth, result)

    while(not trace.isEmpty()):
        v = trace.pop()
        item = v[0]
        depth = v[1]

        if (item.left != 0):
            trace.push((item.left, depth+1))
            add(item.left, depth+1, result)

        if (item.right != 0):
            trace.push((item.right, depth+1))
            add(item.right, depth+1, result)

    return result

target = genBinaryTree(list(range(7)))
printTree(target)
result = linkTranveseTree(target)
print(result)
result = linkTranveseTree(target, True)
print(result)
for i in range(len(result)):
    print("== depth {0} ==".format(i))
    printlist(result[i])
