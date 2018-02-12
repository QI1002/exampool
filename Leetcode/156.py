
#156. Binary Tree Upside Down

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

def updownTree(root):
    if (root == 0): return 0

    s = stack()
    t = root 
    while(t != 0):
      s.push(t)
      t = t.left

    newroot = p = s.pop()
    while(not s.isEmpty()):
        old_p = s.pop()
        p.left = old_p.right
        p.right = old_p
        p = p.right
        old_p.left = old_p.right = 0

    return newroot

sample = [1, 2, 3, 4, 5, None, None, 6, 7]
r = buildTree(sample)
printTree(r)
nr = updownTree(r)
printTree(nr)
