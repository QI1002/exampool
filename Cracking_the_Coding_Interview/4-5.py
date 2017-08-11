
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
    def __init__(self, data, left = 0, right = 0, parent = 0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def genBinaryTree(data):
    count = len(data)
    if (count == 0):
        return 0
    else:
        half = count // 2
        root = tree(data[half])
        root.left = genBinaryTree(data[0:half])
        root.right = genBinaryTree(data[half+1:]) 
        if (root.left != 0):	root.left.parent = root
        if (root.right != 0):	root.right.parent = root
        return root
        
def printTree(root):
    trace = stack()
    trace.push(root)
    while(not trace.isEmpty()):
        item = trace.pop()
        left = "NULL" if item.left == 0 else item.left.data
        right = "NULL" if item.right == 0 else item.right.data
        print("{0}:{1},{2}".format(item.data, left, right))
        if (item.left != 0): trace.push(item.left)            
        if (item.right != 0): trace.push(item.right)
               
def findNode(root, data):
    path = []
    depth = 0  
    trace = stack()
    trace.push((root, depth))    
    while(not trace.isEmpty()):
        v = trace.pop()
        item = v[0]
        depth = v[1]
        
        if (len(path) <= depth):
        	path.append(item)
        else:
        	path[depth] = item
        	path = path[0:depth+1]        	 	
        
        if (item.data == data):
            break
                    
        if (item.left != 0):  trace.push((item.left, depth+1))
        if (item.right != 0): trace.push((item.right, depth+1))
	  
    return path
	  
def findNodeNext(root, data):
    path = findNode(root, data)
    
    item = path[len(path)-1]
    if (item.right != 0): 
        left = item.right
        while(left.left != 0): left = left.left
        return left
          
    while(len(path) != 0):
        item = path.pop()        
        parent = item.parent
        if (parent != 0):
            right = True if parent.right == item else False
            if (right == False):
                return parent;
      
    return 0

def findNodePrev(root, data):
    path = findNode(root, data)
    
    item = path[len(path)-1]
    if (item.left != 0): 
        right = item.left
        while(right.right != 0): right = right.right
        return right
          
    while(len(path) != 0):
        item = path.pop()        
        parent = item.parent
        if (parent != 0):
            right = True if parent.right == item else False
            if (right == True):
                return parent;
      
    return 0
    
total = 22    
target = genBinaryTree(list(range(total)))
printTree(target)
value = 2
result = findNode(target, value)
print(result)
for i in range(len(result)):
    print("depth {0} = {1}".format(i, result[i].data))

item = findNodeNext(target, value)    
print("the next of {0} is {1}".format(value, "NULL" if item == 0 else item.data))

print("=================================")
for i in range(total):    
    item = findNodeNext(target, i)    
    print("the next of {0} is {1}".format(i, "NULL" if item == 0 else item.data))
    
print("=================================")
for i in range(total):    
    item = findNodePrev(target, i)    
    print("the prev of {0} is {1}".format(i, "NULL" if item == 0 else item.data))    