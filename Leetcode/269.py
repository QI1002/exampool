
#269. Alien Dictionary 

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

def getOrder(less):
    if (len(less) == 0): return ""
    aa = []
    bb = []
    for x in less:
        if (not x[0] in aa): aa.append(x[0])
        if (not x[1] in bb): bb.append(x[1])
    cc = []    
    for a in aa:
        if (a in bb): 
            cc.append(a)
    for c in cc:    
        aa.remove(c)
        bb.remove(c)
    #print((aa,bb))
    if (len(aa) != 1 and len(bb) != 1):
        raise ValueError("ambigous")

    a,b = aa[0], bb[0]
    longest = ""
    s = stack()
    s.push(a)
    while(not s.isEmpty()):
        z = s.pop()
        for x,y in less:
            if (x == z[-1]):
                zz = z+y
                if (y == b and len(zz) > len(longest)):
                    longest = zz  
                else:
                    s.push(zz)
    return longest                
            
def alienDict(data):
    less = []
    for i in range(1, len(data), 1):
        j = 0
        a = data[i-1]
        b = data[i]
        while(j < len(a) and j < len(b) and a[j] == b[j]): 
            j += 1
        if (j >= len(a) or j >= len(b)):
            continue
        if (not (a[j],b[j]) in less):
            less.append((a[j],b[j]))
    #print(less)
    return getOrder(less)

data = ["wrt", "wrf", "er", "ett", "rftt"]
print(alienDict(data))
less = [('a','b'),('b','d'),('c','d'),('b','c'),('d','e')]
print(getOrder(less))
less.insert(0, ('a','e'))
print(getOrder(less))
