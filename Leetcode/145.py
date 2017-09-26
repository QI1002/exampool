
#145. Binary Time Postorder Traversal

import random
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

def getTreePostorder(head):
    
    s = stack()
    t = stack()
    result = []
    if (head == 0): return result

    n = head
    while(True):
        while(n != 0):
            s.push(n)
            n = n.left

        if (s.isEmpty()): break
        n = s.pop()
        t.push(n)

        if (n.right == 0): 
            while(not t.isEmpty()): 
                result.append(t.pop().data)
            
        n = n.right

    return result            
          
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
 
root = genBinaryTree(list(range(6)))
root.show()
print(getTreePreorder(root))
print(getTreePostorder(root))
#print(findTreeRecover(root))
