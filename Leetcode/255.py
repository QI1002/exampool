
#255. Verify Preorder Sequence in Binary Search Tree

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

def validPreorder(data):
    if (len(data) == 0): return True

    r = data[0]
    i = 1
    while(i < len(data) and data[i] < r): 
        i+=1

    j = i
    while(j < len(data)):
        if (data[j] < r): return False
        j += 1

    if (validPreorder(data[1:i]) == False): return False
    if (validPreorder(data[i:]) == False): return False
    return True

def buildTree(data):

    if (len(data) == 0): return 0

    r = data[0]
    root = Tree(data[0])
    i = 1
    while(i < len(data) and data[i] < r): 
        i+=1

    j = i
    while(j < len(data)):
        if (data[j] < r): return None
        j += 1

    left = buildTree(data[1:i]) 
    if (left == None): return None
    else: root.left = left
    right = buildTree(data[i:])
    if (right == None): return None
    else: root.right = right
    #print((root, root.left, root.right))

    return root
    
sample = [33, 22, 11, 25, 77, 99, 88]
print(validPreorder(sample[:1]))
print(validPreorder(sample))
print(validPreorder(sample[4:]))
sample = [33, 22, 11, 25, 77, 22, 88]
print(validPreorder(sample))
root = buildTree(sample)
if (root != None): printTree(root)
print(validPreorder(sample[4:]))
sample = [100, 33, 22, 11, 25, 77, 99, 88, 200, 130, 150, 135, 141, 163, 205, 207]
print(validPreorder(sample[:1]))
root = buildTree(sample)
printTree(root)
