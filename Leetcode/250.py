
#250. Count Univalue Subtree

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

def monoTree(root):
    if (root == 0): return True, 0

    v = root.value
    mono = True
    l = r = 0
    if (root.left != 0):
        ll, l = monoTree(root.left)
        if (root.left.value != v): mono = False
        if (ll == False): mono = False

    if (root.right != 0):    
        rr, r = monoTree(root.right)
        if (root.right.value != v): mono = False
        if (rr == False): mono = False

    if (mono == False): 
        return False, l+r
    else:
        return True, 1+l+r
 
sample = [5, 1, 5, 1, 1, None, 5]
sample = [5, 1, 5, 5, 5, None, 5]
r = buildTree(sample)
printTree(r)
print(monoTree(r))

