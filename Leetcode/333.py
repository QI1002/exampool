
#333. Largest BST Subtree

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

def largestBST(root):
    q = []
    q.append(root)
    i = 0
    while(i < len(q)):
        t = q[i]
        i += 1 
        if (t.left != 0): 
            q.append(t.left)

        if (t.right != 0): 
            q.append(t.right)
    
    maxT = None
    for i in range(len(q)-1,-1,-1):
        n = 1
        u = True
        t = q[i]
        if (t.left != 0): 
            nl, ul = t.left.user
            n += nl
            if (ul== False or t.left.value > t.value): 
                u = False
        if (t.right != 0):
            nr, ur = t.right.user
            n += nr 
            if (ur == False or t.right.value < t.value): 
                u = False
        t.user = (n, u)
        #print((t.value, n, u))
        if (u == True):
            if (maxT == None or maxT.user[0] < n):
                maxT = t

    return None if maxT == None else maxT.value,maxT.user[0]        
            
#sample = [ (1,3), (2,3), (3,3), (4,0), (5,0), (6,2), (7,3), (8, 0),
#           (10, 2), (9, 0), (11, 2), (12,0) ]
#sample = [ (5,3), (2,3), (4, 0), (1, 0), (3, 0) ]
sample = [ (50,3), (30, 3), (60, 3), (5, 0), (20, 0), (45, 0), (70, 3),
           (65, 0), (80, 0) ]
r1 = createTree(sample)
#printTree(r1)
print(largestBST(r1))
