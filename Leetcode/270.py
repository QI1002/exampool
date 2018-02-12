
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

def findCloset(root, f):
    s = stack()
    t = root
    while(t != 0):
        s.push(t)
        t = t.left
   
    prev_t = 0
    while(not s.isEmpty()):
        t = s.pop()
        if (float(t.value) == f): return t.value
        if (float(t.value) > f):
            d1 = float(t.value)-f
            d2 = None if prev_t == 0 else f-float(prev_t.value)
            return t.value if (d2 == None or d2 >= d1) else prev_t.value
        prev_t = t
        t = t.right
        while(t != 0):
            s.push(t)
            t = t.left
        
    return prev_t.value

sample = [6, 4, 7, 2, 5, None, None, 1, 3]
r = buildTree(sample)
printTree(r)
nr = buildTree(sample)
nr = flipTree(nr)
printTree(nr)
for f in [2.3, 2.7, 0.2, 7.7]:
    print((findCloset(r, f), findCloset(nr,f)))
