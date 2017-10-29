
#297. Serialize and Deserialize Binary Tree

import copy

class Tree:
    def __init__(self, data, left = 0, right = 0):
        self.data = data
        self.left = left 
        self.right = right


def saveTree(r):
    q = []
    m = []
    v = []
    q.append(r)    
    while(len(q) != 0):
        r = q.pop(0)
        mask = 0
        if (r.left != 0):
            mask |= 0x1
            q.append(r.left)
        if (r.right != 0):
            mask |= 0x2     
            q.append(r.right)
            
        v.append(r.data)    
        m.append(mask)
    
    return (v, m)
    
def loadTree(v, m):

    r = []
    if (len(v) != len(m)):
        raise Exception("value length not match mask length")
        
    j = 0    
    for i in range(len(v)):
        if (len(r) <= i): 
            r.append(Tree(v[j]))        
            j += 1
        if ((m[i] & 0x01) != 0):
            r[i].left = Tree(v[j])
            j += 1            
            r.append(r[i].left)
            
        if ((m[i] & 0x02) != 0):
            r[i].right = Tree(v[j])
            j += 1            
            r.append(r[i].right)
            
    return r[0]              

# d = 1, kinds of tree = 1
# d = 2, kinds of tree = 4 (1+1+1+1*1 = (1+1)^2)
# d = 3, kinds of tree = 25 (1+4+4+4*4 = (4+1)^2)
# d = 4, kinds of tree = 626 (1+25+25+25*25 = (25+1)^2)
def allTree(d = 3, i = 1):

    if (d == 1):  return [Tree(i)]
    
    result = []
    for mask in range(4):
        lt = [0]
        rt = [0]
        if ((mask & 0x1) != 0):
            lt = allTree(d-1, 2*i)
        if ((mask & 0x2) != 0):
            rt = allTree(d-1, 2*i+1)
        r = Tree(i)    
        for k in range(len(lt)):
            for j in range(len(rt)):
                r = Tree(i)
                r.left = lt[k]
                r.right = rt[j]
                                 
                result.append(r)
                          
    return result        
                
    
at = allTree(4)

for t in at:
    v, m = saveTree(t)
    #print((len(v), v, m))
    t2 = loadTree(v, m)
    v2, m2 = saveTree(t2)
    #print((len(v), v2, m2))
    
    match = True
    if (len(v) != len(v2)): 
        print("length v != length v2")        
        match = False
    if (len(m) != len(m2)): 
        print("length m != length m2")
        match = False
    for i in range(len(v)):
        if (v[i] != v2[i]): 
            print("length v[i] != length v2[i]")
            match = False
        if (m[i] != m2[i]): 
            print("length m[i] != length m2[i]")
            match = False

    if (match): print("all match")    