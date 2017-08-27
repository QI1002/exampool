
import random

class seqSearch:
    def __init__(self):
        self.body = []
        self.comp = 0

    def print(self):
        print(self.body)
        
    def search(self, v):
        self.comp = 0
        count = len(self.body)
        for i in range(count):
            self.comp += 1
            if (v <= self.body[i]):
                return i
        return count
                
    def insert(self, v):
        i = self.search(v)
        self.body.insert(i, v)
        
    def delete(self, v):
        i = self.search(v)
        if (i < len(self.body) and self.body[i] == v):
            self.body.pop(i)
    
    def getComp():
        return self.comp
        
class binarySearch(seqSearch):
    def search(self, v):    
        self.comp = 0
        r = len(self.body) - 1
        l = 0
        while (r >= l):
            m = (r+l)//2
            if (self.body[m] == v): 
                return m
                
            self.comp += 1    
            if (m == l):
                if (v < self.body[l]): return l
                return r if (v <= self.body[r]) else r+1
            else:
                if (v > self.body[m]):
                    l = m
                else: 
                    r = m    
        return l  
                                 
class interpoSearch(seqSearch):
    def predict(self, l, r, v):
        m = l                
        if (self.body[r] != self.body[l]):                 
            m += (v-self.body[l])*(r-l)//(self.body[r]-self.body[l])
            m = int(round(m))
            if (l == m and m < r): m = l+1
            if (r == m and m > l): m = r-1            
            #print(r, l, m, v, self.body)   
            
        return m
    
    def predict2(self, l, r, v):
        m = random.randint(l, r)
        if (l == m and m < r): m = l+1
        if (r == m and m > l): m = r-1        
        return m
        
    def search(self, v):
        self.comp = 0
        r = len(self.body) - 1
        l = 0
        while (r >= l):
            
            if (self.body[l] > v):
                return 0
                
            if (self.body[r] < v):
                return len(self.body)

            m = self.predict2(l, r, v)
            if (self.body[m] == v): 
                return m
                
            self.comp += 1                
            if (l == m or r == m):
                if (v < self.body[l]): return l
                return r if (v <= self.body[r]) else r+1
            if (False):
                pass
            else:
                if (v > self.body[m]):
                    l = m
                else:
                    r = m    
        return l
         
class randomSearch(interpoSearch):

    def predict(self, l, r, v):
        m = random.randint(l, r)
        if (l == m and m < r): m = l+1
        if (r == m and m > l): m = r-1        
        return m
                 
class Tree:
    def __init__(self, v, l = 0, r = 0):
        self.v = v
        self.l = l
        self.r = r
 
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
                     
class treeSearch:
    def __init__(self):
        self.head = 0
        self.preorder = 0
        self.inorder = 1
        self.postorder = 2
        self.debug = 3
        self.printSet = {}
        self.printSet[self.preorder] = self.printPreorder
        self.printSet[self.inorder] = self.printInorder
        self.printSet[self.postorder] = self.printPostorder
        self.printSet[self.debug] = self.printDebug
        
    def printPreorder(self):
        s = stack()
        if (self.head != 0): s.push(self.head)
        result = []        
        while(not s.isEmpty()):
            h = s.pop()                    
            result.append(h.v)
            if (h.r != 0): 
                s.push(h.r)
            if (h.l != 0): 
                s.push(h.l)
        print(result)

    def printDebug(self):
        s = stack()
        if (self.head != 0): s.push(self.head)
        result = []        
        while(not s.isEmpty()):
            h = s.pop()                    
            result.append(h.v)
            if (h.r != 0 or h.l != 0):
                print((h.v, None if (h.l == 0) else h.l.v, None if (h.r == 0) else h.r.v))
            if (h.r != 0): 
                s.push(h.r)                
            if (h.l != 0): 
                s.push(h.l)
                

    def getInorder(self):
        s = stack()        
        result = []
        
        n = self.head
        while(n != 0):
            s.push(n)
            n = n.l
        
        while(not s.isEmpty()):
            n = s.pop()
            result.append(n.v)
            n = n.r
            while(n != 0):
                s.push(n)
                n = n.l
        
        return result

    def printInorder(self):
        print(self.getInorder())

    def printPostorder(self):
        s = stack()
        if (self.head != 0): s.push(self.head)
        result = []        
        while(not s.isEmpty()):
            h = s.pop()                    
            result.insert(0, h.v)
            if (h.l != 0): 
                s.push(h.l)
            if (h.r != 0): 
                s.push(h.r)
        print(result)
            
    def print(self, mode = 1):        
        self.printSet[mode]()
                
    def findNext(self, p):
        start = False
        s = stack()        
        result = []
        
        n = self.head
        while(n != 0):
            s.push(n)
            n = n.l
        
        while(not s.isEmpty()):
            n = s.pop()
            if (start): return n
            if (n == p): start = True            
            n = n.r
            while(n != 0):
                s.push(n)
                n = n.l
                        
        return None
                        
    def search(self, v):
        p = n = self.head
        while(n != 0):              
            p = n
            if (v == n.v): break                
            if (n.v > v):
                n = n.l
            else:    
                n = n.r
                
        order = self.getInorder()
        
        if (p.v < v): 
            t = self.findNext(p)
            return len(order) if t == None else order.index(t.v)
        return order.index(p.v)
        
    def insert(self, v):
        if (self.head == 0):
            self.head = Tree(v)
        else:
            n = self.head
            while(n != 0):              
                if (n.v > v):
                    if (n.l == 0): 
                        n.l = Tree(v)
                        break
                    n = n.l
                else:    
                    if (n.r == 0): 
                        n.r = Tree(v)
                        break
                    n = n.r
                                            
    def delete(self, v):
        p = n = self.head
        while(n != 0):              
            if (v == n.v): break                
            
            p = n            
            if (n.v > v):
                n = n.l
            else:    
                n = n.r
                    
        if (n == 0): return

        if (n.r == 0): 
            t = n.l
        else: 
            if (n.r.l == 0):
                t = n.r
                t.l = n.l
            else:
                c = n.r
                while(c.l.l != 0): c = c.l                
                t = c.l
                c.l = t.r
                t.l = n.l
                t.r = n.r
            
        if (n == self.head):
            self.head = t
        else:            
            if (p.v > v):
                p.l = t 
            else: 
                p.r = t       
               
sample = [1,3,4,5,7,10,12,15,16,19,20,25]
template = [4, 1, 16, 3, 7, 15, 25, 19, 10, 5, 12, 20]
#template = []

#searchClass = seqSearch
#searchClass = binarySearch
#searchClass = interpoSearch
#searchClass = randomSearch
searchClass = treeSearch

mySearch = searchClass()
if (len(template) == 0):
    for i in range(len(sample)-1,-1,-1):
        index = random.randint(0, i)
        template.append(sample[index])
        mySearch.insert(sample[index])
        sample.pop(index)
else:
    for i in range(len(sample)):
        mySearch.insert(template[i])
          
print(template)
mySearch.print()
print("===============================")
    
for t in range(27):
    print("search {1} for {0} = {2}".format(t, template, mySearch.search(t)))

print("===============================")
    
#remove = [7, 10, 20, 4 ,19, 16, 5, 15, 12, 1, 25, 3]
remove = []
 
if (len(remove) != 0):
    for i in range(len(remove)):
        t = remove[i]
        mySearch.delete(t)
        print("remove {0} then ".format(t))
        mySearch.print()
else:    
    for i in range(len(template)-1,-1,-1):
        index = random.randint(0, i)
        t = template[index]
        mySearch.delete(t)
        print("remove {0} then ".format(t))
        mySearch.print()    
        template.pop(index)