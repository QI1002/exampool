
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

def flipTree(root):
    if (root == 0): return 0

    s = stack()
    t = root 
    while(t.left != 0):
      s.push(t)
      newroot = t
      t = t.left

    old_p = newroot
    while(not s.isEmpty()):
        p = s.pop()
        if (p == old_p): continue
        p.left = old_p.right
        old_p.right = p
        old_p = p

    return newroot

def findCloset(root, f, k):
    s = stack()
    t = root
    collect = []
    delta = None

    while(True):

        while(t != 0):
            s.push(t)
            t = t.left

        if (s.isEmpty()): break    
        
        t = s.pop()
        if (len(collect) < k): 
            collect.append(t.value)
            d = abs(float(t.value)-f)
            if (delta == None or d > delta): delta = d
        else:
            d = abs(float(t.value)-f)
            if (d >= delta): return collect
            else:
                collect.pop(0)
                collect.append(t.value)
                dd = abs(float(collect[0]-f))
                delta = dd if (dd > d) else d

        t = t.right
        
    return collect

sample = [6, 4, 7, 2, 5, None, None, 1, 3]
r = buildTree(sample)
printTree(r)
nr = buildTree(sample)
nr = flipTree(nr)
for f in [4.3, 4.7, 0.2, 7.7]:
    print((findCloset(r, f, 3), findCloset(nr,f, 3)))
