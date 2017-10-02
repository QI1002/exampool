
#145. Binary Time Postorder Traversal

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

def getTreePreorder(head):
    s = stack()
    result = []
    n = head
    while(True):
        while(n != 0):
            s.push(n)
            n = n.left
        if (s.isEmpty()): break
        n = s.pop()
        result.append(n.data)
        n = n.right
    return result

def getTreePostorder2(head):
    
    if (head == 0): return []
    a = getTreePostorder(head.left)
    b = getTreePostorder(head.right)    
    c = list(a)
    c.extend(b)
    c.append(head.data)
    return c

def getTreePostorder(head):

    s = stack()
    ss = stack()

    if (head == 0): return []

    s.push(head)
    while(not s.isEmpty()):
        n = s.pop()
        ss.push(n.data)
        if (n.right != 0): s.push(n.right)
        else: ss.push([])
        if (n.left != 0): s.push(n.left)
        else: ss.push([])
        while(len(ss.body) >= 3): 
            b = ss.pop()
            a = ss.pop()
            c = ss.pop()
 
            if (type(b) != list or type(a) != list or type(c) != int):
                ss.push(c)
                ss.push(a)
                ss.push(b)
                break

            d = list(a)
            d.extend(b)
            d.append(c)
            ss.push(d)
 
    return ss.pop()
    
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
 
root = genBinaryTree(list(range(7)))
root.show()
print(getTreePreorder(root))
print(getTreePostorder(root))
print(getTreePostorder2(root))
