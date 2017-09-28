
#124. Binary Tree Maxinum Path Sum

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

    def show(self):
        s = stack()
        s.push(self)
        while(not s.isEmpty()):
            l = r = None  
            n = s.pop()
            if (n.left != 0): 
                s.push(n.left)
                l = n.left.data
            if (n.right != 0): 
                s.push(n.right)
                r = n.right.data
            print((n.data, l, r)) 


def getMaxTree(head):
    
    if (head == 0): return 0, 0, [0, 0]

    av, at, ag = getMaxTree(head.left)
    bv, bt, bg = getMaxTree(head.right)

    v = head.data
    maxTree = tree(v)
    if (av > 0): 
        maxTree.left = at
        v += av
    if (bv > 0): 
        maxTree.right = bt
        v += bv

    g = ag if (ag[0] > bg[0]) else bg
    if (v > g[0]):
        g[0] = v
        g[1] = maxTree

    return v, maxTree, g
    
def getMaxTree2(head):

    s = stack()
    ss = stack()

    if (head == 0): return 0, 0, [0, 0]

    globalV = 0
    globalT = 0
    s.push(head)
    while(not s.isEmpty()):
        n = s.pop()
        ss.push(n.data)
        if (n.right != 0): s.push(n.right)
        else: ss.push([0, 0])
        if (n.left != 0): s.push(n.left)
        else: ss.push([0, 0])
        while(len(ss.body) >= 3): 
            b = ss.pop()
            a = ss.pop()
            c = ss.pop()
 
            if (type(b) != list or type(a) != list or type(c) != int):
                ss.push(c)
                ss.push(a)
                ss.push(b)
                break

            v = c
            maxTree = tree(v)
            if (a[0] > 0): 
                maxTree.left = a[1]
                v += a[0]
            if (b[0] > 0): 
                maxTree.right = b[1]
                v += b[0]

            ss.push([v, maxTree])
            if (v > globalV):
                globalV = v
                globalT = maxTree

    result = ss.pop()
    return result[0], result[1], [globalV, globalT]
    
def genBinaryTree(data):
    
    if (len(data) == 0): return 0
    root = tree(data[0])
    q = [ root ]
    i = 1

    while(i < len(data)):    
        t = q.pop(0)
        l = tree(data[i])
        q.append(l)
        t.left = l
        i += 1
        if (i >= len(data)): break
        r = tree(data[i])
        q.append(r)
        t.right = r 
        i += 1
    
    return root
 
root = genBinaryTree([-1, 2, 1, -1, -2, -1, 5])
root.show()
maxV, maxT, maxG = getMaxTree2(root)
print(maxG[0])
maxG[1].show()
