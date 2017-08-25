
import random

def genRandomData(n, m):
    result = []
    while(n > 0):        
        result.append(random.randint(1, m))
        n -= 1
    return result

def genShuffleData(n):
    result = []
    remain = [i for i in range(1,n+1,1)]
    for i in range(n-1, -1, -1):
        index = random.randint(0, i)
        result.append(remain.pop(index))
    return result
    
class heap:
    def __init__(self):
        self.body = [0]
    
    def swap(self, i, j):
        tmp = self.body[i]
        self.body[i] = self.body[j]
        self.body[j] = tmp
        
    def upheap(self):
        i = len(self.body)-1
        while (i != 1):
            p = i // 2
            if (self.body[p] > self.body[i]):
                self.swap(p, i)  
            i = p
                
    def downheap(self, root=1):
        count = len(self.body)-1
        i = root
        c = i+i
        while(c <= count):
            if (c < count and self.body[c] > self.body[c+1]): c += 1
            if (self.body[c] < self.body[i]): 
                self.swap(c, i)
                i = c 
                c = i+i
            else: 
                break  
            
    def push(self, value):
        self.body.append(value)
        self.upheap() 
      
    #NOTICE: check the case that the heap with only one items  
    def pop(self):
        v = self.body[1]
        self.body[1] = self.body[len(self.body)-1]
        self.body.pop()
        self.downheap()
        return v
        
    def sort(self, data):
        result = []
        self.body = [0]
        count = len(data)
        for i in range(count):
            self.body.append(data[i])
            
        for i in range(count//2, 0, -1):
            self.downheap(i)

        for i in range(count):
            result.append(self.pop())
            
        return result    
        
class indirectheap:
    def __init__(self):
        self.body = [0]
        self.index = [0]
        
    def swap(self, i, j):
        tmp = self.index[i]
        self.index[i] = self.index[j]
        self.index[j] = tmp
        
    def upheap(self):
        i = len(self.index)-1
        while (i != 1):
            p = i // 2
            if (self.body[self.index[p]] > self.body[self.index[i]]):
                self.swap(p, i)  
            i = p
                
    def downheap(self, root=1):
        count = len(self.index)-1
        i = root
        c = i+i
        while(c <= count):
            if (c < count and self.body[self.index[c]] > self.body[self.index[c+1]]): c += 1
            if (self.body[self.index[c]] < self.body[self.index[i]]): 
                self.swap(c, i)
                i = c 
                c = i+i
            else: 
                break  
            
    def push(self, value):
        self.index.append(len(self.index))
        self.body.append(value)        
        self.upheap() 
    
    #NOTICE: check the case that the heap with only one items    
    def pop(self):
        top = self.index[1]
        bottom = self.index[len(self.index)-1]
        v = self.body[top]
        self.body[top] = self.body[bottom]
        p = self.index.pop()
        self.body.pop(p)
        for i in range(len(self.body)):
            if (self.index[i] >= p):
                self.index[i] -= 1
        self.downheap()
        return v
        
    def sort(self, data):
        result = []
        self.body = [0]
        count = len(data)
        for i in range(count):
            self.body.append(data[i])
            self.index.append(i)
            
        for i in range(count//2, 0, -1):
            self.downheap(i)

        for i in range(count):
            result.append(self.pop())
            
        return result    
        
def heap_sort(data):
    myheap = heap()    
    count = len(data)
    for i in range(count):
        myheap.push(data.pop())
    
    for i in range(count):
        data.append(myheap.pop())
 
def heap_sort_new(data):
    sortheap = heap()
    result = sortheap.sort(data)

    for i in range(len(data)):
        data[i] = result[i]

def heap_sort_indirect(data):
    myheap = indirectheap()    
    count = len(data)
    for i in range(count):
        myheap.push(data.pop())
    
    for i in range(count):
        data.append(myheap.pop())
 
def heap_sort_indirect_new(data):
    sortheap = indirectheap()
    result = sortheap.sort(data)

    for i in range(len(data)):
        data[i] = result[i]
          
#sort_method = heap_sort
#sort_method = heap_sort_new
#sort_method = heap_sort_indirect
sort_method = heap_sort_indirect_new

target1 = genShuffleData(100)
target2 = genRandomData(100, 20)
target3 = [i for i in range(20, 0, -1)]
target4 = [i for i in range(1,21,1)]
target5 = [5 for i in range(20)]
target6 = [1, 3, 5, 4, 1, 5, 5, 4, 2, 3]
targets = [target1, target2, target3, target4, target5, target6]

for i in range(len(targets)):
    print(targets[i])
    sort_method(targets[i])
    print(targets[i])
    print("=================================")