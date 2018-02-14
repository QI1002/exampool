
#270. Closest Binary Search Tree Value

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

class Tree:
    def __init__(self, v):
        self.left = 0
        self.right = 0
        self.value = v
        self.user = None

def buildTree(data):
    nodes = [ ] 
    for x in data: 
        t = 0 if x == None else Tree(x)
        nodes.append(t)

    for i in range(len(data)):
        t = nodes[i]
        if (t == 0): continue
        l = 2*(i+1)-1
        if (l < len(data)): t.left = nodes[l] 
        r = 2*(i+1)
        if (r < len(data)): t.right = nodes[r]
    
    return nodes[0]

def printTree(root):
    print("==================")
    s = stack()
    s.push(root)
    while(not s.isEmpty()):
        t = s.pop()
        r = None 
        if t.right != 0 :
            r = t.right.value
            s.push(t.right)
        l = None 
        if t.left != 0 : 
            l = t.left.value
            s.push(t.left)
        print((t.value, l, r))

def createTree(data):
    q = []
    i = 0
    v, m = data[i]
    root = Tree(v)
    q.append(root)
    q.append(m)
    while(i < len(data)):
        if (len(q) == 0): break
        t = q.pop(0)
        m = q.pop(0)
        if ((i+1) < len(data) and (m & 1) != 0):
            i += 1
            t.left = Tree(data[i][0])
            q.append(t.left)
            q.append(data[i][1])
        if ((i+1) < len(data) and (m & 2) != 0):
            i += 1
            t.right = Tree(data[i][0])
            q.append(t.right)
            q.append(data[i][1])

    return root

def findLongestSeq(root):
    q = []
    q.append(root)
    maxu = 0
    while(len(q) > 0):
        u = 0
        t = q.pop(0)
        if (t.left != 0): 
            q.append(t.left)
            if (t.left.value == (t.value+1)):
                if (t.user == None): t.user = 1
                t.left.user = t.user + 1
                if (t.left.user > maxu): maxu = t.left.user
        if (t.right != 0): 
            q.append(t.right)
            if (t.right.value == (t.value+1)):
                if (t.user == None): t.user = 1
                t.right.user = t.user + 1
                if (t.right.user > maxu): maxu = t.right.user

    return maxu            
            
sample = []
for x in range(1,8,1): sample.append((x,3))
for x in range(8,16,1): sample.append((x,0))
r1 = createTree(sample)
#printTree(r1)
print(findLongestSeq(r1))
sample = [(1,2),(3,3),(2,0),(4,2),(5,0)]
r2 = createTree(sample)
#printTree(r2)
print(findLongestSeq(r2))
sample = [(2,2),(3,1),(2,1),(1,0)]
r3 = createTree(sample)
#printTree(r3)
print(findLongestSeq(r3))
sample = []
for x in [1,2,9,3,6,10,11]: sample.append((x,3))
for x in [4,5,7,8,12,13,14,15]: sample.append((x,0))
r4 = createTree(sample)
#printTree(r4)
print(findLongestSeq(r4))

