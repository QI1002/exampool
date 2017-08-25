

#95. Unique Binary Search Trees II

import math 

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
    def __init__(self, left, right):
        self.left = left 
        self.right = right
            
def getAllTrees(n):
       
    if (n == 0): 
        return [0]
           
    if (n == 1):
        return [Tree(0, 0)]
    
    result = []

    for i in range(n):
        left = getAllTrees(i)
        right = getAllTrees(n-i-1)
        for j in range(len(left)):
            for k in range(len(right)):  
                root = Tree(left[j], right[k])
                result.append(root)
                
    return result
    
def toTreeList(root):
    result = []
    trees = stack()
    trees.push((root, 0, 1))
    while(not trees.isEmpty()):
        item = trees.pop()        
        node = item[0]
        value = item[1]*2+item[2]
        result.append(value)         
        if (node.right != 0):  trees.push((node.right, value, 1)) 
        if (node.left != 0):  trees.push((node.left, value, 0))  
              
    return result
    
def toTreeGraph(root, d):
    step = 1 << d 
    prefix = step >> 1
    count = 1
    index = 1
    data = toTreeList(root)
    print(data)
    for i in range(d):
        for j in range(count):
            star = "*" if (index in data) else " "                
            if (j == 0):
                line = " " * (prefix-1) + star
            else:
                line += " " * (step-1) + star                  
            index += 1            
        print(line)          
        count <<= 1      
        step >>= 1
        prefix = step >> 1
            
alltrees = getAllTrees(4)           
for i in range(len(alltrees)):
#   print(toTreeList(alltrees[i]))
    toTreeGraph(alltrees[i], 4)    
