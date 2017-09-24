
#99 Recover Binary Search Tree

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

def getTree(head):
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
          
def genBinaryTree(data):
    count = len(data)
    if (count == 0):
        return 0
    else:
        half = count // 2
        root = tree(data[half])
        root.left = genBinaryTree(data[0:half])
        root.right = genBinaryTree(data[half+1:])  
        return root
 
def switchNode(data):
    i = random.randint(0, len(data)-1)
    while(True):
        j = random.randint(0,len(data)-1)
        if (i != j): break

    temp = data[i]
    data[i] = data[j]
    data[j] = temp
    return data
            
def findRecover(data):
    r1 = -1
    r2 = -1
    for i in range(1, len(data), 1): 
        if (data[i] < data[i-1]):
            if (r1 == -1):
                r1 = i-1
                r2 = i
            else:
                r2 = i   
        
    return data[r1], data[r2]     

def findTreeRecover(head):
    s = stack()
    r1 = -1
    r2 = -1 
    prev = None   
    n = head
    while(True):
        while(n != 0):
            s.push(n)
            n = n.left
        if (s.isEmpty()): break
        n = s.pop()
        if (prev != None and n.data < prev.data):
            if (r1 == -1):
                r1 = prev
                r2 = n
            else:
                r2 = n
        prev = n
        n = n.right
    return r1.data, r2.data   
    
sample = switchNode(list(range(1,7,1)))
print(sample)
print(findRecover(sample))
root = genBinaryTree(sample)
print(getTree(root))
print(findTreeRecover(root))